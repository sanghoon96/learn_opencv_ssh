import cv2 as cv
import numpy as np

img = cv.imread("datas/images/lena.png")
print(img.shape)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(imgGray.shape)

grayToBGR = cv.cvtColor(imgGray, cv.COLOR_GRAY2BGR)
print(grayToBGR.shape)

imgHor = np.hstack((grayToBGR, img))
# cv.imshow("Horizontal", imgHor)
print(imgHor.shape)

imgVer = np.vstack((grayToBGR, img))
# cv.imshow("Vertical", imgVer)
print(imgVer.shape)

imgVer2 = np.vstack((img, grayToBGR))
# cv.imshow("Vertical2", imgVer2)

imgVer3 = np.flipud(imgVer)
# cv.imshow("FlipVer", imgVer3)

imgHorVer = np.hstack((imgVer, imgVer2, imgVer))
cv.imshow("Hor + Ver", imgHorVer)
print(imgHorVer.shape)

imgVerFlip = np.hstack((imgVer, imgVer3, imgVer))
cv.imshow("Ver + Flrip", imgVerFlip)
cv.waitKey(0)