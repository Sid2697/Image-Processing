import cv2
import numpy as np

img=cv2.imread('Pb.jpg',1)
img1=cv2.imread('Pb1.jpg',1)

add1 = img+img1
add=cv2.add(img,img1) #It adds up all the pixels
weighted = cv2.addWeighted(img, 0.3, img1, 0.7,1)

cv2.imshow('Add',add1)
cv2.imshow('Weighted',weighted)
cv2.imshow('Image',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
