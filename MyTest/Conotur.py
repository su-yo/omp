import cv2
import numpy as np
orgImage = cv2.imread('GroupProjects.png')
tempImage = cv2.cvtColor(orgImage, cv2.COLOR_BGR2GRAY)
thresh = tempImage
cv2.threshold(tempImage, 127, 255, 0, thresh)
cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(orgImage,contours,-1,(0,255,0),3)
#cv2.imshow('bgimage', ret)
cv2.waitKey(0)
