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
