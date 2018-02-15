import sys 														#This line is used for Linking OpenCV with Python3
sys.path.append('/usr/local/lib/python3.5/site-packages')
import cv2
import numpy as np


img = cv2.imread('Pb.jpg',1)

img[100,120]=[0,0,0]
pix=img[100,120]
roi = img[100:150, 100:150]=[0,0,0] # Region of Image
copy=img[37:111,107:194]
img[0:74,0:87]=copy

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()