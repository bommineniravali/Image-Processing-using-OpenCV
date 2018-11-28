import cv2 
import sys
import numpy as np 
  
# Reading the input image 
img = cv2.imread(sys.argv[1], 0) 
kernel = np.ones((5,5), np.uint8) 
#reduces the white region
img_erosion = cv2.erode(img, kernel, iterations=1)
cv2.imwrite("img_erosion.jpg",img_erosion) 
#increases the white region
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite("img_dilation.jpg",img_dilation)
#ersion followed bt dilation
img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite("img_opening.jpg",img_opening)
#Dilation followed by ersion
img_closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imwrite("img_closing.jpg",img_closing)
#diff b/w dilation and ersion
img_gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("img_gradient.jpg",img_gradient)
#diff b/w opening of image and input image
img_tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite("img_tophat.jpg",img_tophat)
#diff b/w closing and input
img_blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imwrite("img_blackhat.jpg",img_blackhat)


