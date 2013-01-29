import cv2
cv2.namedWindow('a_window', cv2.CV_WINDOW_AUTOSIZE)
image = cv2.imread('GroupProjects.png', cv2.CV_LOAD_IMAGE_COLOR)
cv2.imshow('a_window', image)
cv2.waitKey(0)
cv2.imwrite('image.png', image)
