# Code to generate various shapes in The image
import cv2
import numpy as np

img = cv2.imread('iphone.jpg',1)
cv2.line(img, (10,0),(1000,900), (12,66,14),15,cv2.LINE_AA)
cv2.rectangle(img,(9,9),(900,900),(45,90,180),6)
cv2.circle(img, (500,500),200,(100,0,0),5,cv2.LINE_AA)

pts=np.array([[100,500],[203,560],[1,1000],[999,0]], np.int32)
cv2.polylines(img, [pts],True, (0,255,255),3)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Siddhant Bansal', (330,99),font,1.4,(124,225,89),1,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
