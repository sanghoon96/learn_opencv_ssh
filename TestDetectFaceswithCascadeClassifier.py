import os
import cv2 as cv

path = os.getcwd()
print(path)

cascade = cv.CascadeClassifier(path + "/datas/haar_cascade_files/haarcascade_frontalface_default.xml")
cascade_eye = cv.CascadeClassifier(path + "/datas/haar_cascade_files/haarcascade_eye.xml")
# cascade_nose = cv.CascadeClassifier(path + "/datas/haar_cascade_files/haarcascade_mcs_nose.xml")

img = cv.imread(path + "/datas/images/faces.jpg")

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(imgGray, 1.1, 4)
eyes = cascade_eye.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    
for (a, b, c, d) in eyes:
    cv.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 2)

img_resize = cv.resize(img, (1280,960))

cv.imshow("Result", img_resize)
cv.waitKey(0)