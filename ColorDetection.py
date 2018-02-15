import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([150, 150, 00])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((50, 50), np.float32) / 225   	# Averaging for making the resultant image more smooth
    smooth = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (15, 15), 0)  # Gaussian Blur
    median = cv2.medianBlur(res, 15)  # Median Blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)  # Bilateral Filter

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('Smooth', smooth)
    cv2.imshow('Blur', blur)
    cv2.imshow('Median', median)
    cv2.imshow('Bilateral', bilateral)

    if cv2.waitKey(2) & 0xFF == ord(' '):
        break

cv2.destroyAllWindows()
cap.release()
