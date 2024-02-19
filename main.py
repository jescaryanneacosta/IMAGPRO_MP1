import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

data_dir = "/data"

resized_images = []

for filename in os.listdir(data_dir):
    img = cv2.imread(os.path.join(data_dir, filename))
    img_resized = cv2.resize(img, (32, 32))
    resized_images.append(img_resized)

images_array = np.array(resized_images)

plt.figure(figsize=(10, 10))
for i in range(len(images_array)):
    plt.subplot(2, 3, i+1)
    plt.imshow(cv2.cvtColor(images_array[i], cv2.COLOR_BGR2RGB))
    plt.axis('off')
plt.show()

print("Shape of the resulting variable:", images_array.shape)
