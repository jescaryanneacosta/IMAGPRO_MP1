import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

def visualize_images(image_tensor, indices):
    plt.figure(figsize=(10, 5))
    for i, idx in enumerate(indices):
        plt.subplot(1, len(indices), i + 1)
        plt.imshow(image_tensor[idx])
        plt.title(f"Image {idx}")
        plt.axis('off')
    plt.show()

def compute_euclidean_distances(image_tensor):
    euclidean_distances = np.zeros((len(image_tensor), len(image_tensor)))
    for i in range(len(image_tensor)):
        for j in range(i+1, len(image_tensor)):
            euclidean_distances[i, j] = euclidean(image_tensor[i].flatten(), image_tensor[j].flatten())
            euclidean_distances[j, i] = euclidean_distances[i, j]
    return euclidean_distances

def analyze_distances(euclidean_distances):
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(euclidean_distances)
    
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(euclidean_distances)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], c=clusters, cmap='viridis')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('PCA Visualization of Euclidean Distances')
    plt.colorbar(label='Cluster')
    plt.show()

image_tensor = np.load("image_tensor.npy")

visualize_images(image_tensor, [1, 3, 5])

euclidean_distances = compute_euclidean_distances(image_tensor)

analyze_distances(euclidean_distances)
