import cv2 as cv
img = cv.imread("datas/images/lena.png")        # 이 경로는 vscode 기준으로 함
# DISPLAY
cv.imshow("Lena Soderberg",img)
cv.waitKey(10000)               # 창 띄우는 시간