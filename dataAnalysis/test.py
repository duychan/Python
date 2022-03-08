import numpy as np
arr_zeros = np.zeros(10)
arr_ones = np.ones(10)
arr_fives = np.ones(10)*5
arr_fitty = np.arange(10,51)
matrix_33 = np.arange(0,9).reshape(3,3)
matrix_inf = np.identity(3)
randomNum = np.random.rand(1,1)
random25 = np.random.randn(1,25)
matrix_100 = np.arange(1,101).reshape(10,10)*0.01
linear_20 = np.linspace(0,1,20)
arr = np.array([[16,17,18,19,20],[21,22,23,24,25]])
total = np.sum(arr)
total2 = np.sum(arr,axis=0)
arr2 = np.arange(1,33).reshape(8,4)
print(arr2[[0,1,2,3,4]] [1:])