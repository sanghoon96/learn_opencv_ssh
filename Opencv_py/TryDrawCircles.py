import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("./datas/images/load_image.jpg")
plt.figure()

cv.rectangle(img, (52, 80), (110,114), (0,0,255), 2)
cv.putText(img, "Hand", (114,93), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

cv.circle(img, (240, 103), 40, (0,0,255), 2)
cv.putText(img, "Head", (209,45), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

cv.rectangle(img, (393, 236), (466,293), (0,0,255), 2)
cv.putText(img, "Foot", (471,252), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

cv.rectangle(img, (327, 282), (393,337), (0,0,255), 2)
cv.putText(img, "Ball", (331,282), cv.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

cv.circle(img, (71, 300), 20, (255,0,0), cv.FILLED)
cv.line(img, (71,300), (img.shape[0],img.shape[1]), (255,0,0), 3)

plt.imshow(img[:,:,::-1])
plt.show()


cv.destroyAllWindows()

# cv.imshow("Messi",img)
# cv.waitKey(0)

# -------------------------- Method 1 ----------------------------------------------
# def mouse_callback(event, x, y, flags, param): 
#     print("마우스 좌표, x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력

# img = cv.imread("./datas/images/load_image.jpg")
# mask = np.zeros((342, 548, 3), np.uint8)  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)
# cv.namedWindow('image')  #마우스 이벤트 영역 윈도우 생성
# cv.setMouseCallback('image', mouse_callback)

# while(True):
#     cv.imshow('image', img)
#     k = cv.waitKey(1) & 0xFF
#     if k == 27:    # ESC 키 눌러졌을 경우 종료
#         print("ESC 키 눌러짐")
#         break

# cv.destroyAllWindows()
