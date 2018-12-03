import cv2
import sys

image=cv2.imread(sys.argv[1])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,100,200)
cv2.imshow("edges",edges)
cv2.imwrite("edges.jpg",edges)
cv2.waitKey(0)
