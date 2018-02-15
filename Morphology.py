import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	
	lower_white=np.array([150,150,00])
	upper_white=np.array([255,255,255])
	mask = cv2.inRange(hsv,lower_white,upper_white)
	res=cv2.bitwise_and(frame,frame,mask=mask)
	
	kernel=np.ones((5,5),np.uint8)
	erosion=cv2.erode(mask, kernel, iterations =1)
	dilation =cv2.dilate(mask, kernel, iterations =1)
	
	opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)	
	
	cv2.imshow('frame',frame)
	cv2.imshow('res',res)
	cv2.imshow('erosion',erosion)
	cv2.imshow('dilation',dilation)
	cv2.imshow('opening',opening)
	cv2.imshow('closing',closing)	
	
	if cv2.waitKey(2) & 0xFF == ord(' '):
		break
		
cv2.destroyAllWindows()
cap.release()