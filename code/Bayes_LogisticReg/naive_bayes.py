import pandas as pd
import numpy as np
import collections as cc
import re
from sklearn.model_selection import train_test_split

def data_preprocess(filename, split_ratio):
    data = pd.read_csv(filename, skiprows=1, header=None)   # Skip the headline
    features = data.iloc[:, :-1]    # Pick all columns except last column as features
    classes = data.iloc[:, -1]  # Pick last column as classes
    x_train, x_test, y_train, y_test = train_test_split(features, classes, train_size = split_ratio, random_state = 0)
    return x_train, y_train, x_test, y_test

class Multinomial_NB():
    def __init__(self):
        self.features = []
        self.classes = []
        self.unfeats = []
        self.prior = dict() # Used to store prior probabilities
        self.labels = dict()
        self.loglh = dict() # Used to store loglikehood 
  
    def countlabels(self, label):
        cnt = 0
        for idx, _docs in enumerate(self.features):
            if (self.classes[idx] == label):
                cnt += 1
        return cnt

    # Count all known features
    def countallfeatures(self):
        features = []
        for feature in self.features:
            features.extend(feature) 
        return np.unique(features)

    def countfeaturesbyclass(self, label):
        features = []
        for idx, doc in enumerate(self.features):
            if self.classes[idx] == label:
                features.extend(doc)
        if label not in self.labels:
            self.labels[label]=features
        else:
            self.labels[label].append(features)

    def fit(self, X, Y, save = False):
        # Convert training set as a sentence (string format), e.g. [1 2 3 4] to ["1 2 3 4 "]
        X = [" ".join(item) for item in np.array(X).astype(str)]
        Y = [" ".join(item) for item in np.array(Y).astype(str)]
        self.features = X
        self.classes = Y
        self.unfeats = self.countallfeatures()
        for label in np.unique(self.classes):
            self.prior[label] = np.log(self.countlabels(label) / len(self.features))    # Calculate prior probabilities for classes
            self.countfeaturesbyclass(label)
            feature_counter = cc.Counter(self.labels[label])
            total_count = len(self.labels[label])
            for word in self.unfeats:
                # Implement Laplace smoothing
                self.loglh[word, label] = np.log((feature_counter[word] + 1)/(total_count + len(self.unfeats)))

    def predict(self, new):
        new = [" ".join(item) for item in np.array(new).astype(str)]
        ret = []
        prior = self.prior
        unfeature = self.unfeats
        likehood = self.loglh
        classes = self.classes
        for doc in new:
            uniqlabel = np.unique(classes)
            probs = dict()
            for label in uniqlabel:
                probs[label] = prior[label]
                for word in doc:
                    if word in unfeature:
                        probs[label] += likehood[word, label]
            result = np.argmax(list(probs.values()))    # Pick the max probability label
            ret.append(uniqlabel[result])
        return ret
   
if __name__=="__main__":
    X_train, Y_train, X_test, Y_test = data_preprocess('/home/lgr/Workspace/CS235/numerical.csv', 0.8)
    MNB = Multinomial_NB()
    MNB.fit(X_train, Y_train)
    labels = MNB.predict(X_test)    # Get the test results
    count = 0
    for i in range(len(labels)):    # Compare with testset labels
        if labels[i] == str(np.array(Y_test)[i]):
            count += 1
    print("Accuracy: ", count / len(X_test))