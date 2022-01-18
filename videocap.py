import numpy as np
import cv2 as cv
cap1 = cv.VideoCapture(1)
cap2 = cv.VideoCapture(2)
cap3 = cv.VideoCapture(3)
if not cap1.isOpened() or cap2.isOpened() or cap3.isOpened() :
    print("Cannot open one or more cameras")
    exit()
while True:
    # Capture frame-by-frame
    frame1 = cap1.read()
    frame2 = cap2.read()
    frame3 = cap3.read()
    # if frame is read correctly ret is True
    if not frame1 or not frame2 or not frame3 :
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    gray3 = cv.cvtColor(frame3, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('CAM 1', gray1)
    cv.imshow('CAM 2', gray2)
    cv.imshow('CAM 3', gray3)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()