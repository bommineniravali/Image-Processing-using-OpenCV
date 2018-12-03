import cv2
c=1
vc = cv2.VideoCapture('YUV.yuv')
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
while rval:
	rval, frame = vc.read()
	if rval:
		image=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
		cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
		cv2.imwrite(str(c) + '.jpg',frame)
		cv2.imshow('frame',image)
		c = c + 1
	if cv2.waitKey(0) & 0xFF == ord('q'):
		break
vc.release()
