import cv2 as cv
import numpy as np

# contours are the boundaries of objects
# from math, theyre not edges. 
# They're the points that connect edges.
img = cv.imread('../resources/photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')

cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# cv.imshow('Blur', blur)

# # Grab the edges of the photo
canny = cv.Canny(blur, 125, 175)

# cv.imshow('Canny', canny)

# looks are the structures found, or the edges
# and returns two values. 

# retrlist finds all contours in the image
# external retrieves only the external ones (outside)
# retrtree finds all hiterarchal contours 
# approx ind

# hierarchies are the contours nested in eachother
 
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)}')

cv.imshow('Thresh', canny)

cv.drawContours(blank, contours, -1, (0,0,255), 1)

cv.imshow('Contours Drawn', blank)

cv.waitKey(0)