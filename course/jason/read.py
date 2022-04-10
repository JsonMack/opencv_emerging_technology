import cv2 as cv

# Reads image
img = cv.imread('../resources/photos/cat.jpg')

# Shows image - imshow(windowName, pi)
cv.imshow('Cat', img)

# Waits for keyboard key to be pressed
cv.waitKey(0)
