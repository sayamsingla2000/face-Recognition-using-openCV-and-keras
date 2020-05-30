# Simple program to read and showw image
import cv2

img = cv2.imread('dog.png')
gray = cv2.imread('dog.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Dog Image',img)
cv2.imshow('gray dog image',gray)

cv2.waitKey(0) #program will stop when any key is pressed
cv2.destroyAllWindowa()