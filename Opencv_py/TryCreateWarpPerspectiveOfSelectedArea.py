import cv2 as cv
import numpy as np

img1 = cv.imread("datas/images/licenseplate_01.jpg")
img2 = cv.imread("datas/images/licenseplate_02.jpg")

width,height = 700,350
pts1 = np.float32([[321,313],[515,319],[321,356],[513,358]]) 
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
img1Output = cv.warpPerspective(img1,matrix,(width,height))

width,height = 700,350
pts3 = np.float32([[270,243],[395,240],[269,269],[395,267]]) 
pts4 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts3,pts4)
img2Output = cv.warpPerspective(img2,matrix,(width,height))


cv.imshow("Image1",img1)
cv.imshow("Output1",img1Output)

cv.imshow("Image2",img2)
cv.imshow("Output2",img2Output)

import matplotlib.pyplot as plt
plt.imshow(img1[:,:,::-1])
plt.imshow(img2[:,:,::-1])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()