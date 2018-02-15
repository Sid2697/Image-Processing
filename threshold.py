import sys
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 12,225,cv2.THRESH_BINARY)
retval, threshold1 = cv2.threshold(img1, 12,225,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)


cv2.imshow('Original',img)
cv2.imshow('Threshold',threshold)
cv2.imshow('Threshold1',threshold1)
cv2.imshow('gaus',gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
