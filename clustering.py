import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD RFM DATA
# ==========================================

rfm = pd.read_csv("output/customer_rfm.csv")

print("=" * 60)
print("OPTIMAL CLUSTER ANALYSIS")
print("=" * 60)

print("RFM Dataset Shape:")
print(rfm.shape)

print()


# ==========================================
# 2. SELECT FEATURES
# ==========================================

features = [
    "Recency",
    "Frequency",
    "Monetary"
]

X = rfm[features].copy()

print("Features:")
print(features)

print()


# ==========================================
# 3. LOG TRANSFORMATION
# ==========================================

X_log = np.log1p(X)

print("Log transformation completed.")

print()


# ==========================================
# 4. STANDARDIZATION
# ==========================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X_log)

print("Standardization completed.")

print()


# ==========================================
# 5. ELBOW METHOD
# ==========================================

inertia_values = []

k_values = range(2, 11)

for k in k_values:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    inertia_values.append(kmeans.inertia_)


# ==========================================
# 6. PRINT INERTIA
# ==========================================

print("Elbow Method Results:")
print()

for k, inertia in zip(k_values, inertia_values):

    print(
        f"K = {k} | "
        f"Inertia = {inertia:.2f}"
    )

print()


# ==========================================
# 7. ELBOW GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    list(k_values),
    inertia_values,
    marker="o"
)

plt.title("Elbow Method for Optimal K")

plt.xlabel("Number of Clusters (K)")

plt.ylabel("Inertia")

plt.xticks(list(k_values))

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "output/elbow_method.png"
)

plt.show()


# ==========================================
# 8. SILHOUETTE SCORE
# ==========================================

silhouette_scores = []

print("Silhouette Scores:")
print()

for k in k_values:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    silhouette_scores.append(score)

    print(
        f"K = {k} | "
        f"Silhouette Score = {score:.4f}"
    )

print()


# ==========================================
# 9. SILHOUETTE GRAPH
# ==========================================

plt.figure(figsize=(10, 6))

plt.plot(
    list(k_values),
    silhouette_scores,
    marker="o"
)

plt.title("Silhouette Score for Different K")

plt.xlabel("Number of Clusters (K)")

plt.ylabel("Silhouette Score")

plt.xticks(list(k_values))

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "output/silhouette_scores.png"
)

plt.show()


# ==========================================
# 10. BEST K
# ==========================================

best_index = np.argmax(silhouette_scores)

best_k = list(k_values)[best_index]

best_score = silhouette_scores[best_index]

print("=" * 60)

print("BEST CLUSTER COUNT")

print("=" * 60)

print(f"Best K: {best_k}")

print(f"Best Silhouette Score: {best_score:.4f}")

print()

print("=" * 60)

print("OPTIMAL CLUSTER ANALYSIS COMPLETED")

print("=" * 60)
