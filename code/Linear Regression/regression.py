import numpy as np
import matplotlib.pyplot as plt

def ridge(X,Y,lam): #ridge regression
    myeye = np.eye(X.shape[1])
    myeye[0][0] = 0
    return np.linalg.solve(X.T@X + lam*myeye,X.T@Y)

rawdata = pd.read_csv('C:/Users/HP/Desktop/CLASS/CS235/proj/new_covidDataset/Daegu_alldata.csv')
rawdata = np.asarray(rawdata)
#print(rawdata)
originy = rawdata[:,[2]]
originy = np.array(originy,dtype='float')

x = rawdata[:,[3,4,5]]#train set
x = np.array(x,dtype='float')
xtest = rawdata[:,[6,7,8]] #test set
xtest = np.array(xtest,dtype = 'float')

w = ridge(x,originy,1)#do ridge regression
testy = xtest@w #get testy

axisx = []
for i in range(x.shape[0]):
    axisx.append(i)
ty = []
tx = []
for i in range(x.shape[0]-60):
    ty.append(originy[i+60])
    tx.append(axisx[i+60])
py = []
for i in range(x.shape[0]-60):
    py.append(testy[i+60])

plt.plot(axisx, originy, color = 'red', linestyle = 'solid', label = 'training confirmed cases')
plt.plot(xtest, testy, color = 'blue', linestyle = 'dashed', label = 'predicting confirmed cases')
plt.plot(tx, ty, color = 'yellow', linestyle = 'solid', label = 'real confirmed cases')
plt.title('# of Coronavirus Cases Over Time', size=20)
plt.xlabel('Days Since 1/20/2020', size=20)
plt.ylabel('# of Cases', size=20)
plt.legend()
#plt.xticks(size=10)
#plt.yticks(size=10)
plt.show()



