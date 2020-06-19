import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def data_preprocess(filename, split_ratio):
    data = pd.read_csv(filename, skiprows=1, header=None)   # Skip the headline
    features = data.iloc[:, :-1]    # Pick all columns except last column as features
    classes = data.iloc[:, -1]  # Pick last column as classes
    x_train, x_test, y_train, y_test = train_test_split(features, classes, train_size = split_ratio, random_state = 0)
    return x_train, y_train, x_test, y_test

class Logistic_Regression:
    def __init__(self):
        self.theta = None
    
    def sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))
    
    # Take advantage of matrix operations in numpy
    def fit(self, X, Y, times = 1000, step = 0.05):
        X = np.mat(X)   # Convert training set as matrix
        XT = X.T    # Transpose matrix
        Y = np.mat(Y)
        m, n = np.shape(X)
        self.theta = np.mat(np.ones(n)) # Initial theta values
        for i in range(times):
            self.theta -= step / m * (self.sigmoid(self.theta * XT) - Y) * X
    
    def predict(self, new):
        probs = self.sigmoid(self.theta * np.mat(new).T)
        return probs

if __name__=="__main__":
    X_train, Y_train, X_test, Y_test = data_preprocess('/home/lgr/Workspace/CS235/numerical.csv', 0.7)
    LR = Logistic_Regression()
    LR.fit(X_train, Y_train)
    probs = LR.predict(X_test).tolist()
    count = 0
    for i in range(len(probs[0])):  # If the probability is more than 50%, then consider it should be label 1
        if probs[0][i] > 0.5 and np.array(Y_test)[i] == 1.0:
            count += 1
        elif probs[0][i] <= 0.5 and np.array(Y_test)[i] == 0.0:
            count += 1
    print("Accuracy: ", count / len(X_test))
