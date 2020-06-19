import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#names = ['confirmed','latitude','longitude']
#read data
datal = pd.read_csv('D:\\CS235\\project\\dataset\\new_covidDataset\\Case-csv2.csv')
datal.head()
correlation=datal.corr()
#jointpoint figure
sns.jointplot(x = 'latitude', y = 'confirmed', data = datal ,kind = 'reg')
sns.jointplot(x = 'longitude', y = 'confirmed', data = datal ,kind = 'reg')
#Heat map can be used to show the correlation between multiple variables
sns.heatmap(correlation, cmap="YlGnBu",vmax=1, vmin=0, annot=True)
plt.show()