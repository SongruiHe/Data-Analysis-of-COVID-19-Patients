from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt


# Test K=1-9 and find the best K
def find_best_k(subDataset):
    SSE = []
    for k in range(1, 9):
        km = KMeans(n_clusters=k)
        km.fit(subDataset)
        SSE.append(km.inertia_)

    X = range(1, 9)
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.plot(X, SSE, 'o-')
    plt.show()


# Implement sklean Kmeans
def km_sk(subDataset):
    km = KMeans(n_clusters=3)
    km.fit(subDataset)
    df['cluster'] = km.labels_
    df.to_csv('clustered.csv')


if __name__ == '__main__':
    df = pd.read_csv('afterEncoding_std.csv')
    subDataset = df.loc[:, ['sex', 'age', 'country', 'province', 'city', 'disease', 'infection_case']]
    find_best_k(subDataset)
    km_sk(subDataset)
