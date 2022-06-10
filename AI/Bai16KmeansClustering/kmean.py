import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# from sklearn.cluster import KMeans


class Kmean:
    def __init__(self, link_data, features, K, max_iters=10):
        data = pd.read_csv(link_data)
        X = data[features]
        X = np.array(X)

        print(X)

        centroids, idx = self.find_k_means(X, K)
        
        self.idx = idx
        self.centroids = centroids

    def initialize_K_centroids(self, X, K):
        m,n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[np.random.choice(range(len(X)), K, replace=False),:]
        return k_rand

    def find_closest_centroids(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids

    def find_k_means(self, X, K, max_iters=10):
        _, n = X.shape
        centroids = self.initialize_K_centroids(X, K) 
        centroid_history = np.zeros((max_iters, K, n))
        for i in range(max_iters):
            idx = self.find_closest_centroids(X, centroids)
            centroids = self.compute_means(X, idx, K)
        
        return centroids, idx
        