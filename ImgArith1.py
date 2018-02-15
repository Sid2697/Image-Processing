import cv2
import numpy as np

img = cv2.imread('iphone.jpg')
img1 = cv2.imread('iphone.jpg')

rows,cols,channels=img.shape
roi=img[0:rows,0:cols]



img2gray=cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_TRIANGLE) # PIXEL VALUE ABOVE 220 IS CONVERTED TO 225 BELOW 220 IS CONVERTED TO BLACK

mask_inv=cv2.bitwise_not(mask)

img_bg=cv2.bitwise_and(roi,roi, mask=mask_inv)
img1_fg=cv2.bitwise_and(img1,img1, mask=mask)

dst = cv2.add(img_bg,img1_fg)
img[0:rows,0:cols]=dst

cv2.imshow('img_bg',img_bg)
cv2.imshow('dst',dst)
cv2.imshow('img1_fg',img1_fg)
cv2.imshow('res',img)
cv2.imshow('Mask_inv',mask_inv)
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
