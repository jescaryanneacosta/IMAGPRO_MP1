import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

def amp_and_att(image):
    amplified_image = image * 0.3
    attenuated_image = image / 0.3

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(amplified_image.astype(np.uint8))
    plt.title("Amplified Image")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(attenuated_image.astype(np.uint8))
    plt.title("Attenuated Image")
    plt.axis('off')

    plt.show()

def multiplication(image):
    multiplication_factors = [0.1, 0.2, 0.5, 1.0]
    multiplied_images = []

    for factor in multiplication_factors:
        multiplied_images.append(image * factor)

    plt.figure(figsize=(12, 6))
    for i, img in enumerate(multiplied_images):
        plt.subplot(1, len(multiplied_images), i + 1)
        plt.imshow(img.astype(np.uint8))
        plt.title(f"Factor: {multiplication_factors[i]}")
        plt.axis('off')

    plt.show()

def euclidean_distances(image_tensor):
    euclidean_distances = np.zeros((len(image_tensor), len(image_tensor)))

    for i in range(len(image_tensor)):
        for j in range(i+1, len(image_tensor)):
            euclidean_distances[i, j] = euclidean(image_tensor[i].flatten(), image_tensor[j].flatten())
            euclidean_distances[j, i] = euclidean_distances[i, j]

    print("Euclidean Distances Matrix:")
    print(euclidean_distances)

def main():
    image_tensor = np.load("image_tensor.npy")

    amp_and_att(image_tensor[0])

    multiplication(image_tensor[0])

    euclidean_distances(image_tensor)

