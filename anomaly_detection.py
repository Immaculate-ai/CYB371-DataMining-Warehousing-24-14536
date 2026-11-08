"""Anomaly detection demonstrations on generated normal and unusual observations."""

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
from sklearn.cluster import DBSCAN
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler


def z_score_flags(X, threshold=2.5):
    """Flag a row if any feature is more than threshold standard deviations away."""
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    std[std == 0] = 1
    scores = np.abs((X - mean) / std)
    return np.any(scores > threshold, axis=1)


def run():
    print("\n[5] ANOMALY DETECTION")
    print("Example: identify unusual network activity measurements.")

    rng = np.random.default_rng(21)
    normal = rng.normal(loc=0, scale=1, size=(180, 3))
    unusual = np.array([[5.5, 5.0, 4.8], [-5.2, 4.9, 5.1], [6.0, -5.5, 5.5]])
    X = np.vstack([normal, unusual])
    X_scaled = StandardScaler().fit_transform(X)

    detectors = {
        "Isolation Forest": IsolationForest(contamination=0.02, random_state=21),
        "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, contamination=0.02),
        "One-Class SVM": OneClassSVM(nu=0.02, gamma="scale"),
    }

    for name, detector in detectors.items():
        if name == "Local Outlier Factor":
            predictions = detector.fit_predict(X_scaled)
        else:
            predictions = detector.fit_predict(X_scaled)
        count = int(np.sum(predictions == -1))
        print(f"{name:25s} possible anomalies = {count}")

    dbscan_labels = DBSCAN(eps=0.9, min_samples=6).fit_predict(X_scaled)
    print(f"{'DBSCAN noise points':25s} possible anomalies = {int(np.sum(dbscan_labels == -1))}")

    flags = z_score_flags(X_scaled, threshold=2.5)
    print(f"{'Z-Score method':25s} possible anomalies = {int(flags.sum())}")

    # Simple neural-network autoencoder demonstration:
    # Train on the normal observations only, then flag high reconstruction errors.
    normal_scaled = StandardScaler().fit(normal)
    normal_train = normal_scaled.transform(normal)
    all_scaled = normal_scaled.transform(X)
    autoencoder = MLPRegressor(
        hidden_layer_sizes=(2,), activation="relu", solver="adam",
        max_iter=1500, random_state=21, early_stopping=False
    )
    autoencoder.fit(normal_train, normal_train)
    reconstructed = autoencoder.predict(all_scaled)
    errors = np.mean((all_scaled - reconstructed) ** 2, axis=1)
    cutoff = np.quantile(
        np.mean((normal_train - autoencoder.predict(normal_train)) ** 2, axis=1),
        0.98
    )
    print(f"{'Autoencoder (MLP)':25s} possible anomalies = {int(np.sum(errors > cutoff))}")


if __name__ == "__main__":
    run()
