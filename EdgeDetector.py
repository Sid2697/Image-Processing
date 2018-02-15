import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	Black=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	edges=cv2.Canny(frame,100,130)

	cv2.imshow('Edges',edges)

	if cv2.waitKey(2) & 0xFF == ord(' '):
		break


cv2.destroyAllWindows()
cap.release()
