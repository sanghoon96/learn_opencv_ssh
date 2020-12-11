import cv2 as cv
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)

try:
    while(cap.isOpened()):
        success, img = cap.read()
        cv.imshow("Result", img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv.waitKey(1) & 0xFF == ord('i'):
            img = cv.imread("datas/images/lena.png")        # 이 경로는 vscode 기준으로 함
            # DISPLAY
            cv.imshow("Lena Soderberg",img)
            cv.waitKey(10000)
        elif cv.waitKey(1) & 0xFF == ord('v'):
            cap = cv.VideoCapture("datas/videos/Armbot.mp4")
            while True:
                success, img = cap.read()
                img = cv.resize(img, (frameWidth, frameHeight))
                cv.imshow("Result", img)
# except:
#     while(cap.isOpened()):
#         if cv.waitKey(1) & 0xFF == ord('v'):
#             cap = cv.VideoCapture("datas/videos/Armbot.mp4")
#             while True:
#                 success, img = cap.read()
#                 img = cv.resize(img, (frameWidth, frameHeight))
#                 # frameWidth = frameWidth + 20
#                 # frameHeight = frameHeight + 20
#                 cv.imshow("Result", img)
except:
    print("Error : Exception")

finally:
    cap.release()
    cv.destroyAllWindows()