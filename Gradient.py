import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	Black=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	laplacian=cv2.Laplacian(Black, cv2.CV_64F)
	sobelx=cv2.Sobel(Black,cv2.CV_64F,1,0,ksize=5)
	sobely=cv2.Sobel(Black,cv2.CV_64F,0,1,ksize=5)
	
		
	cv2.imshow('Original',frame)
	cv2.imshow('Laplacian',laplacian)
	cv2.imshow('sobelx',sobelx)
	cv2.imshow('sobely',sobely)	
	
		
	k = cv2.waitKey(5)&0xFF
	if cv2.waitKey(2) & 0xFF == ord(' '):
		break
		
cv2.destroyAllWindows()
cap.release()
