import cv2 as cv
import numpy as np

# image 불러오기
img = cv.imread("datas/images/lena.png")
# cv.imshow("Image", img) # 이미지가 잘 불러와지는지 확인만 하고 주석처리
print(img.shape)

# camera 불러오기
camera = cv.VideoCapture(0) # web cam device0번 사용
cam_wid = camera.get(cv.CAP_PROP_FRAME_WIDTH) # 카메라 width 사이즈 확인
cam_hei = camera.get(cv.CAP_PROP_FRAME_HEIGHT) # 카메라 height 사이즈 확인
print(cam_wid) # float임으로 int로 변경 필요
print(cam_hei)

# camera size resize하기
wid = 640
hei = 480
cam_resize_wid = camera.set(cv.CAP_PROP_FRAME_WIDTH, wid)
cam_resize_hei = camera.set(cv.CAP_PROP_FRAME_HEIGHT, hei)
# print(camera.shape) # 에러 출력, 이유는 camera는 array가 아니라 하나의 class 객체이기 때문에 shape가 찍히지 않는다.
# print(type(camera))

# image resize 하기 (기준은 카메라 resize한 것을 기준으로)
img_resize = cv.resize(img, (wid, hei))
print(img_resize.shape)

while camera.isOpened():
    success, cam = camera.read()
    # h,w,c = cam.shape # h = 480, w = 640, c = 3
    mer_img_cam = np.hstack((img_resize, cam))

    cv.imshow("Result", mer_img_cam)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
