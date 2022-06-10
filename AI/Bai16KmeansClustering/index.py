from kmean import Kmean

kmean = Kmean('./iris-dataset.csv', ['sepal_length','sepal_width','petal_length','petal_width'], 4)
print(kmean.centroids)
print(kmean.idx)