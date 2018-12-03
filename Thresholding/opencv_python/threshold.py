import cv2
import sys

src= cv2.imread(sys.argv[1])
image = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
_,dst = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
cv2.imwrite("thres_binay.jpg",dst)
_,thrsh_binary_inv = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imwrite("thrsh_binary_inv.jpg",thrsh_binary_inv)
_,dst=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)
cv2.imwrite("thresh_trunc.jpg",dst)
_,dst=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
cv2.imwrite("thresh_tozero.jpg",dst)
_,dst=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
cv2.imwrite("thresh_tozero_inv.jpg",dst)
dst=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,9)
cv2.imwrite("adaptive_mean.jpg",dst)
dst=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,17,9)
cv2.imwrite("adaptive_gaussian.jpg",dst)
