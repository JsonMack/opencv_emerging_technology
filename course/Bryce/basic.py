import cv2 as cv

img = cv.imread('../Resources/Photos/cat.jpg')

cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur an image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow('Eroded', eroded)

# resize
# default = cv.INTER_AREA, best used for making smaller images.
# when making image larger cv.INTER_LINEAR or cv.INTER_CUBIC.
# cubic is slower but higher quality
resized = cv.resize(img, (500, 100), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
