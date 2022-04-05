import cv2 as cv
import numpy as np

img = cv.imread('../resources/photos/group 1.jpg')
cv.imshow('Group',img)

# Convert to grayscale - The intensity distribution of pixels
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Cat',gray)

# Blur an image - remove some of the noise - increase blur with kernel size (x,x)
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge cascade - find the edges that are present in the img
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# Reduce the amount of edges by blurring the img first
cannyR = cv.Canny(blur, 125, 175)
# cv.imshow('CannyR', cannyR)

# Dilating the img
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# Erode the img
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize the img with a built in function
resized = cv.resize(img, (500,500))
# cv.imshow('Resized', resized)

# Crop the img - specify what sections should be in the frame
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)