import cv2 as cv
import numpy as np

# Create a blank img for drawing (h, w, col-channel)
blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('../resources/photos/cat.jpg')
# cv.imshow('Cat', img)

# Paint the blank green
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# Paint only a section of pixels (range : range)
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red Square', blank)

# Paint a rectangle
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2) # for a border
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=cv.FILLED) # for a filled in rectangle
# cv.imshow('Rectangle', blank)

# Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (0,0,255), thickness=2)
# cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
# cv.imshow('Line', blank)

# Write some text
cv.putText(blank, 'Canvas', (190,285), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)