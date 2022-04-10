import cv2 as cv

# Captures a video from the
capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    # frame reads in each frame of the video, isTrue says if the frame was read in or not
    isTrue, frame = capture.read()
    
    # read and display the video frame by frame
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# if (-215: Assertion failed) -> opencv could not find a media file at the specified location
# Once all the frames from the video have rendered, opencv could not find anymore frames
# This will also occur for images with an invalid path