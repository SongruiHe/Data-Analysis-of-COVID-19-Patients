import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)
#read data
datal = pd.read_csv('D:\\CS235\\project\\dataset\\new_covidDataset\\Case-csv.csv')
datal.head()
#bar plot figure
sns.barplot(x = 'group', y ='confirmed', data = datal)

plt.show()