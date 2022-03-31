import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')

# draw rect with thickness of 2 from origin with defined size
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 0), thickness=-1)

# draw circle with given center
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 64, (0, 0, 255), thickness=4)


# draw a line on the image
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=4)

cv.putText(blank, 'Hello world', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), thickness=2)

cv.imshow('Text', blank)

cv.waitKey(0)

