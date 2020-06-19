from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pylab

def ridge(X,Y,lam):
    myeye = np.eye(X.shape[1])
    myeye[0][0] = 0
    return np.linalg.solve(X.T@X + lam*myeye,X.T@Y)

def gend(rawdata,i):
    if rawdata[i][2] == 'male':
        male.append(rawdata[i][3])
    if rawdata[i][2] == 'female':
        female.append(rawdata[i][3])
male = []
female = []
rawdata = pd.read_csv('C:/Users/HP/Desktop/CLASS/CS235/proj/new_covidDataset/TimeGender.csv')
rawdata = np.asarray(rawdata)
for i in range(rawdata.shape[0]):
    gend(rawdata,i)

dates = []
for i in range(rawdata.shape[0]):
    dates.append(i)
dates = np.arange(len(dates)/2).reshape(-1, 1)
male = np.asarray(male)
female = np.asarray(female)
dates = np.asarray(dates)

plt.plot(dates, male, color = 'red', linestyle = 'solid', label = 'male')
plt.plot(dates, female, color = 'blue', linestyle = 'solid', label = 'female')

plt.title('# of Coronavirus Cases Over Gender', size=20)
plt.xlabel('Days Since 3/2/2020', size=20)
plt.ylabel('# of Cases', size=20)
plt.legend()
#plt.xticks(size=10)
#plt.yticks(size=10)
plt.show()




