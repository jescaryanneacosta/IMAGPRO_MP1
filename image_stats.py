import numpy as np

image_tensor = np.load("image_tensor.npy")

for i, image in enumerate(image_tensor):
    print(f"Results for Image {i + 1}:")
    total_pixels = image.shape[0] * image.shape[1] * image.shape[2]
    average_pixel_per_channel = np.mean(image, axis=(0, 1))
    normalized_image = image / 255.0
    pixels_lessequalto = np.sum(normalized_image <= 0.5)
    
    print("Total number of pixels:", total_pixels)
    print("Average pixel value per channel:", average_pixel_per_channel)
    print("Number of pixels equal to 0.5 and less than 0.5:", pixels_lessequalto)
