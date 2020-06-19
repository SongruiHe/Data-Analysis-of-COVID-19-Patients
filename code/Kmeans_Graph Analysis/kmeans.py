import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random as rand


def myKmeans(data, K, max_iter=500, tol=0.00001):
    cluster_number = []
    sse = []

    # Random initial centroids
    centroids = rand.sample(data, K)

    iters = 0
    for i in range(max_iter):
        iters += 1
        cluster_number = []

        # Initialize clusters
        clusters = [[] * K for j in range(K)]

        find_closest_centroid(data, centroids, cluster_number, clusters)
        error = compute_sse(data, cluster_number, centroids)
        sse.append(error)

        # Convergence
        if np.absolute(sse[i] - sse[i - 1]) / sse[i - 1] <= tol and i > 0:
            break

        # Find new centroids
        for i, cluster in enumerate(clusters):
            centroids[i] = np.mean(cluster, axis=0).tolist()

    return cluster_number


def find_closest_centroid(data, centroids, cluster_number, clusters):
    for data_point in data:
        min_distance = float('inf')
        closest_cluster = 0

        # Find the closest centroid for each data point
        for i, centroid in enumerate(centroids):
            # Calculate the distance between data_point and centroid
            distance = np.linalg.norm(np.array(data_point) - np.array(centroid))
            if distance < min_distance:
                closest_cluster = i
                min_distance = distance

        cluster_number.append(closest_cluster)
        clusters[closest_cluster].append(data_point)


# Compute SSE during iteration
def compute_sse(data, cluster_number, centroids):
    errors = []
    for i, data_point in enumerate(data):
        error = np.linalg.norm(np.array(data_point) - np.array(centroids[cluster_number[i]]))
        errors.append(error ** 2)

    return sum(errors)


if __name__ == '__main__':
    df = pd.read_csv('afterEncoding_std.csv')
    subDataset = df[['sex', 'age', 'country', 'province', 'city', 'disease', 'infection_case']].values.tolist()

    result = myKmeans(subDataset, 3)
    print(result)
