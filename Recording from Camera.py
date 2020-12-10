import cv2 as cv
import os

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out_avi = cv.VideoWriter('datas/videos/output.avi',fourcc, 20.0, (540,480))
fourcc = cv.VideoWriter_fourcc(*'MP4V')
out_mp4 = cv.VideoWriter('datas/videos/output.mp4',fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    out_avi.write(frame)
    out_mp4.write(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
out_avi.release()
out_mp4.release()