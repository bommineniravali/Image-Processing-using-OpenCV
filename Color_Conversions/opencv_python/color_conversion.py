import cv2
import sys
image=cv2.imread(sys.argv[1])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.namedWindow("hsv",cv2.WINDOW_NORMAL)
cv2.imshow("hsv",hsv)
cv2.waitKey(0)
