import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture("datas/videos/Armbot.mp4")
while True:
    success, img = cap.read()
    img = cv.resize(img, (frameWidth, frameHeight))
    # frameWidth = frameWidth + 20
    # frameHeight = frameHeight + 20
    cv.imshow("Result", img)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()