"""Clustering algorithms using generated customer-like data."""

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift
from sklearn.mixture import GaussianMixture


def run():
    print("\n[2] CLUSTERING")
    print("Example: group customers by two measured behaviour features.")
    X, _ = make_blobs(n_samples=180, centers=3, cluster_std=0.75, random_state=12)
    X = StandardScaler().fit_transform(X)

    models = {
        "K-Means": KMeans(n_clusters=3, n_init=10, random_state=12),
        "Hierarchical (Agglomerative)": AgglomerativeClustering(n_clusters=3),
        "DBSCAN": DBSCAN(eps=0.35, min_samples=5),
        "Mean Shift": MeanShift(),
        "Gaussian Mixture Model": GaussianMixture(n_components=3, random_state=12),
    }

    for name, model in models.items():
        if name == "Gaussian Mixture Model":
            labels = model.fit_predict(X)
        else:
            labels = model.fit_predict(X)
        clusters = len(set(labels) - {-1})
        noise = int(np.sum(labels == -1))
        print(f"{name:30s} clusters found = {clusters}, noise points = {noise}")


if __name__ == "__main__":
    run()
