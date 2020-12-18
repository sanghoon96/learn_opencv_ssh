from cv2 import cv2 as cv
import numpy as np

def getContours(img, img_rgb):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv.contourArea(cnt)
        
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            
            cv.drawContours(img_rgb, [approx], 0, (255,0,0),5)
            cv.imshow('tmp', img_rgb)
            # cv.waitKey()

            objCor = len(approx)
            x, y, w, h = cv.boundingRect(approx)

            objectType = None
            if objCor == 4:
                objectType = "Rectangle"
            elif w == h:
                objectType = "Square"

            if objCor == 8:
                objectType = "Circle"
            
            if objectType:
                cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 0, 0), 2)


path = 'datas/images/snapshots/3b18352c-3ffb-11eb-8ec8-16f63a1aa8c9.jpg'
img = cv.imread(path)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)

imgContour = img.copy()
getContours(imgCanny, img)

cv.imshow('detected shapes', imgContour)

cv.waitKey(0)
cv.destroyAllWindows()