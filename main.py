import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

folder_path = "C:/Users/Jesca Ryanne Acosta/Documents/GitHub/IMAGPRO_MP1/data"

resized_images = []

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = cv2.imread(os.path.join(folder_path, filename))
        resized_img = cv2.resize(img, (32, 32))
        resized_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB)
        resized_images.append(resized_img)

image_tensor = np.array(resized_images)

plt.figure(figsize=(10, 5))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(image_tensor[i])
    plt.title(f"Image {i+1}")
    plt.axis('off')
plt.show()

print("Shape of the resulting variable:", image_tensor.shape)

np.save("image_tensor.npy", image_tensor)
