import numpy as np

image_tensor = np.load("image_tensor.npy")

first_image = image_tensor[0]

total_pixels = first_image.shape[0] * first_image.shape[1] * first_image.shape[2]

average_pixel_per_channel = np.mean(first_image, axis=(0, 1))

normalized_image = first_image / 255.0
pixels_lessequalto = np.sum(normalized_image <= 0.5)

print("Total number of pixels in the first image:", total_pixels)
print("Average pixel value per channel:", average_pixel_per_channel)
print("Number of pixels equal to 0.5 and less than 0.5:", pixels_lessequalto)
