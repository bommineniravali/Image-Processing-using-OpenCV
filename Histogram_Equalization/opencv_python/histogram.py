import cv2
import sys
image=cv2.imread(sys.argv[1])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.equalizeHist(image)
cv2.imshow("equalizeHist", image)
cv2.imwrite("equalizeHist.jpg",image)
cv2.waitKey(0)