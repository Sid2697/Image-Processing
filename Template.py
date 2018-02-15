import cv2
import numpy as np

main = cv2.imread('temp_test.jpg')
BW=cv2.cvtColor(main,cv2.COLOR_BGR2GRAY)
temp = cv2.imread('temp_test1.jpg',0)
w,h=temp.shape[::-1]

res=cv2.matchTemplate(BW,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.72
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
	cv2.rectangle( main,pt,(pt[0]+w,pt[1]+h),(0,255,255),2) 
 	
cv2.imshow('Detected',main)
cv2.waitKey(0)
cv2.destroyAllWindows()
