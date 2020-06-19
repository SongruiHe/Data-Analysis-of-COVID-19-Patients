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

def regi(rawdata,i,area):
    if area == 'Seoul':
        Seoul.append(rawdata[i][3])
    if area == 'Busan':
        Busan.append(rawdata[i][3])
    if area == 'Daegu':
        Daegu.append(rawdata[i][3])
    if area == 'Incheon':
        Incheon.append(rawdata[i][3])
    if area == 'Gwangju':
        Gwangju.append(rawdata[i][3])
    if area == 'Daejeon':
        Daejeon.append(rawdata[i][3])
    if area == 'Ulsan':
        Ulsan.append(rawdata[i][3])
    if area == 'Sejong':
        Sejong.append(rawdata[i][3])
    if area == 'Gyeonggi-do':
        Gyeonggi_do.append(rawdata[i][3])
    if area == 'Gangwon-do':
        Gangwon_do.append(rawdata[i][3])
    if area == 'Chungcheongbuk-do':
        Chungcheongbuk_do.append(rawdata[i][3])
    if area == 'Chungcheongnam-do':
        Chungcheongnam_do.append(rawdata[i][3])
    if area == 'Jeollabuk-do':
        Jeollabuk_do.append(rawdata[i][3])
    if area == 'Jeollanam-do':
        Jeollanam_do.append(rawdata[i][3])
    if area == 'Gyeongsangbuk-do':
        Gyeongsangbuk_do.append(rawdata[i][3])
    if area == 'Gyeongsangnam-do':
        Gyeongsangnam_do.append(rawdata[i][3])
    if area == 'Jeju-do':
        Jeju_do.append(rawdata[i][3])

Seoul = []
Busan = []
Daegu = []
Incheon = []
Gwangju = []
Daejeon = []
Ulsan = []
Sejong = []
Gyeonggi_do = []
Gangwon_do = []
Chungcheongbuk_do = []
Chungcheongnam_do = []
Jeollabuk_do = []
Jeollanam_do = []
Gyeongsangbuk_do = []
Gyeongsangnam_do = []
Jeju_do = []

rawdata = pd.read_csv('C:/Users/HP/Desktop/CLASS/CS235/proj/new_covidDataset/TimeProvince.csv')
rawdata = np.asarray(rawdata)
for i in range(rawdata.shape[0]):
    regi(rawdata,i,rawdata[i][2])

dates = []
for i in range(102):
    dates.append(i)


plt.plot(dates, Seoul, color = 'red', linestyle = 'solid', label = 'Seoul')

plt.plot(dates, Busan, color = 'yellow', linestyle = 'solid', label = 'Busan')

plt.plot(dates, Daegu, color = 'blue', linestyle = 'solid', label = 'Daegu')

plt.plot(dates, Gyeonggi_do, color = 'green', linestyle = 'solid', label = 'Gyeonggi-do')

plt.plot(dates, Gyeongsangbuk_do, color = 'black', linestyle = 'solid', label = 'Gyeongsangbuk-do')


plt.title('# of Coronavirus Cases Over Region', size=20)
plt.xlabel('Days Since 1/20/2020', size=20)
plt.ylabel('# of Cases', size=20)
plt.legend()
#plt.xticks(size=10)
#plt.yticks(size=10)
plt.show()

'''
xtrain = np.arange(len(datestrain)).reshape(-1, 1)
w = ridge(xtrain,y,0.1)
xtest = []
ytest = []
for i in range(40):
    ytest.append(confirmed[i+confirmed.shape[0]-40][3])
    xtest.append(confirmed[i+confirmed.shape[0]-40][0])
xtest = np.arange(len(xtest)).reshape(-1, 1)
for i in range(len(xtest)):
    xtest[i]+=confirmed.shape[0]-40
ypred = xtrain@w


poly = PolynomialFeatures(degree = 4)
linear_model = LinearRegression()
linear_model.fit(xtrain, y)
xtest = np.arange(len(dates) + 10).reshape(-1, 1)
X_test_poly = poly.transform(xtest)
predictions = linear_model.predict(X_test_poly)
plt.figure(figsize=(10, 5))
'''


