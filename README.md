# IMAGPRO_MP1
Goal: Apply theories from linear algebra and signal processing to understanding images.

Action items:
<p>
1. [Matrix Analysis] Resize the images from this datasetLinks to an external site. into 32 by 32 matrices then aggregate them into one variable.
Visualize the images using Pyplot.
The result should be (6,32,32,3)
Explain the shape of the resulting variable and the quality of the images
Determine the shape of the images.
Save the tensor as an .npy file
</p>

[Image Statistics] Take the first image:
How many pixels are there in total?
Take the average of each pixel per channel.
How many pixels are equal to 0.5 and less than 0.5?
Clue 1: normalize the image first.
Clue 2: Create a histogram for the image. The total number of bins should match the nominal pixel values of a grayscale image.
Report the results for the images and your image.
[Basic Signal Processing] Take the first image:
Apply amplification and attenuation operations onto the image by a factor of 0.3.
What did you notice? What does the operation imply?
Try to do element-wise multiplication of the values 0.1, 0,2, 0.5, and 1.0 to the image.
What happened?
Inspect the values of the matrix and determine the error
Resolve the error using your knowledge of matrix algebra and signal processing. Explain your solution.
Compute the Euclidean distances between all of the images.
What were the values?
What did you observe from images 1, 3, and 5? Experiment further and discuss your findings.