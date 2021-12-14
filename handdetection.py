import numpy as np
import cv2

hand= cv2.imread('0.jpg' , 0)
cv2.imshow('original',hand)
h=hand
ret ,threshold= cv2.threshold(hand, 50 ,255, cv2.THRESH_BINARY)
contours, hierarchy= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
hull=[cv2.convexHull(c) for c in contours]
final=cv2.drawContours(threshold,hull,-1,(255,255,255))
f=cv2.drawContours(h,hull,-1,(255,255,255))

cv2.imshow('threshold',threshold)
#cv2.imshow('final',h)
cv2.waitKey(0)
