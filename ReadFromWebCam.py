import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(2)

cap.set(cv.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, frameHeight)
cap.set(cv.CAP_PROP_BRIGHTNESS,150)
while cap.isOpened():
    success, img = cap.read()
    if success == False:
        break
    # else:
    #     for (i=2, i>2, i++;)
    #         cv.VideoCapture(i)
    cv.imshow("Result", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()