import cv2
import numpy as np
cv2.namedWindow('Histogram_Equalized', cv2.CV_WINDOW_AUTOSIZE)
orgImage = cv2.imread('scaled.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
tempImage = orgImage
cv2.equalizeHist(orgImage, tempImage)
cv2.imshow('Histogram_Equalized', tempImage)
cv2.waitKey(0)

