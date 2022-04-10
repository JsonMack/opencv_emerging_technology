import cv2 as cv

img = cv.imread('../Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)


def rescale_frame(frame, scale=0.75):
    # recorded video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_res(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)
    

# Reading Video
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame, 0.1)

    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
