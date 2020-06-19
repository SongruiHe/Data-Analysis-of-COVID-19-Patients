In Data Preprocess folder:
numerical.java implements extracting sex, age, country, province, infection case, infection order and state features from dataset and make them numerical so that use them as the input in SVM method.
numericTool_std.py implements the encoding and standardizing process using sklearn.
How to run:
1. Edit file path
2. Run


In Correlation Analysis folder:
environment: Python 3.7
How to run
1. Edit read filePath in correlation.py correlation2.py and corrPatient.py
2. run
correlation.py: joint plot regression graph of longitude,latitude and number of patients, heatmap
correlation2.py: bar plot
corrPatient.py: another heat map


In SVM folder:
environment: Java 1.8
how to run code: 
1.edit input file path in main.java
2.compile and run main.java
dataUtil.java provides all the data processing methods.
svm.java implements SVM method with SMO algorithm.
kernalFunction.java and linearKernal.java provide an interface that can implement more kernel functions but in this project, only implement linear kernel function, because time is limited and the environment makes me feel too stressful to concentrate on implementing other methods. So, these classes are just saved for scalability in the future.
main.java is the entrance of the code and includes OVO multi-classification method.


In Bayes & LogisticReg folder:
Implement of Multinomial Naive Bayes algorithm and Logistic Regression algorithm.
Only use library for basic functions such as dataset split, matrix operations. The cores of algorithms are clear written in code.
Just run these python codes in environment which has installed library pandas, numpy, collections, re(regular expression) and sklearn.model_selection (Only use for split dataset).


In Linear Regression folder:
region.py evaluates the confirmed cases across different cities, and sex.py evaluates the gender percentage across the confirmed cases.
regression.py implements extracting temperature, humidity and virus spread trend from dataset, and use ridge regression to train the train set, then use test set to make prediction. 
Environment: Python3.6
How to run code:
1. Edit input filepath in regression.py
2. Run regression.py


In Kmeans&Graph Analysis folder:
kmeans.py implements our own kmeans algorithm.
kmeans_sklearn.py implements the kmeans algorithm by sklearn and finding the optimal K.
spread_graph_community.py implements the community detection and central nodes detection methods.
spread_graph_std.py implements the community detection method.
How to run:
1. Edit input path(the input data is after preprocessed)
2. Run each python file.