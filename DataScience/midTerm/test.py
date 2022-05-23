import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('BIKE DETAILS.csv')
arrData = data['selling_price'].to_numpy()
n = 7 #sample size
M = 15000 #number of boostrap sampling  

arrSTD = []
for _ in range(M):
    rowData = arrData[np.random.randint((len(data)), size= n)]
    stdRow = np.std(rowData)
    arrSTD.append(stdRow)
    
alpha = 0.95
p = ((1.0-alpha)/2.0) * 100
lower =  np.percentile(arrSTD, p)
p = (alpha+((1.0-alpha)/2.0)) * 100
upper =  np.percentile(arrSTD, p)
confidenceIntervalRange = [lower,upper]
print(confidenceIntervalRange)
sns.displot(arrSTD, kde = True)
plt.axvline(x= lower, color='r')
plt.axvline(x= upper, color='r')

plt.show()