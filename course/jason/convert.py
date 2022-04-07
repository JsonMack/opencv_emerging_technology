import cv2 as cv;

img = cv.imread('../resources/photos/park.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)

# cv.imshow('Canny', canny)

dilated = cv.dilate(canny, (3, 3), iterations=1)

cv.imshow('Dilated', dilated)

cv.waitKey(0)