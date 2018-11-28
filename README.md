# Image-Processing-using-OpenCV

#Image_Blurring

1)Gaussian Blurring:Gaussian blurring is highly effective in removing gaussian noise from the image.
Parameters:
src	input image.
dst     output image.
ksize	Gaussian kernel size.
sigma	Gaussian standard deviation both x and y direction.

2)Median Blurring:takes median of all the pixels under kernel area and central element is replaced with this median value.This is highly effective against salt-and-pepper noise in the images.
Parameters:
src	input image.
dst     output image.
ksize	linear size; it must be odd and greater than 1, for example: 3, 5, 7 ...

3)Bilateral Filtering:is highly effective in noise removal while keeping edges sharp.
src	input image.
dst     output image.
ksize	Filter size.
sigmaColor  Filter sigma in the color space.
sigmaSpace  Filter sigma in the coordinate space.

#Morphological Dilation and Erosion using OpenCV
1)Dilation:It increases the white region in the image or size of foreground object increases.
2)Erosion:Simply white region decreases in the image. It is useful for removing small white noises,detach two connected objects etc.
3)Opening:Erosion followed by dilation.It is useful in removing noise
4)Closing:Dilation followed by Erosion.It is useful in closing small holes inside the foreground objects
5)Morphological Gradient:It is the difference between dilation and erosion of an image.
6)Top Hat:It is the difference between input image and Opening of the image.
7)Black Hat:It is the difference between the closing of the input image and input image.

Application level:
->Eliminate noise in the image (Removing noise)
->Isolation of individual elements and joining disparate elements in an image.
->Finding the essence of the largest object or the smallest area (Finding of brightness bumps or holes in an image)
#Histogram Equalization
Histogram Equalization is a image processing technique used to improve contrast in images.



