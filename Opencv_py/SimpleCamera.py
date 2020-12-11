import cv2 as cv

cap = cv.VideoCapture(0)

try:
    # Read until video is completed
    while(cap.isOpened()):
    # while(1):                # occur Error              
        # Capture frame-by-frame
        ret, frame = cap.read()     # Capture frame-by-frame

        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) == 27:             # 27 is ESC on keyboard
            break
except :
    pass
finally:
        # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

print('End....')