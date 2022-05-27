import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('BIKE DETAILS.csv')
data.replace({'1st owner':1, '2nd owner':2, '3rd owner':3, '4th owner':4}, inplace=True)
labels = ['1st owner', '2nd owner', '3rd owner', '4th owner']
data['owner'].value_counts().plot.pie(autopct='%.1f%%')
x = data['owner'].value_counts()
plt.legend(labels,
          title="owner",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()