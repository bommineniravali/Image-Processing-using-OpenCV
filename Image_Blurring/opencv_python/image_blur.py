import cv2
import sys

image=cv2.imread(sys.argv[1])
gaussianblur=cv2.GaussianBlur(image,(5,5),0)
cv2.imwrite("GaussianBlur.jpg",gaussianblur)
bilateralfilter=cv2.bilateralFilter(image,9,75,75)
cv2.imwrite("bilateralfilter.jpg",bilateralfilter)
median = cv2.medianBlur(image,5)
cv2.imwrite("median.jpg",median)
cv2.imshow("input",image)
cv2.waitKey(0);