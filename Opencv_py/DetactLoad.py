import cv2 as cv, numpy as np
import os,time


def nothing():
    return 0

def frame_diff(prev_frame,cur_frame):
    diff_frame = cv.absdiff(prev_frame,cur_frame)
    return diff_frame


if __name__ == "__main__":  

    cv.namedWindow("Edge")
    cv.createTrackbar("low threshold","Edge",160,255,nothing)
    cycle = True

    cap = cv.VideoCapture(os.getcwd()+"/datas/videos/roadway_01.mp4")  
    hei = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    wid = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))     
    prev_img = np.zeros((hei,wid),dtype=np.uint8)


    if cap.grab():
        _,img = cap.read()
        img = cv.cvtColor(img[int(img.shape[0]/2):,:],cv.COLOR_BGR2GRAY)
        low = 133
        high = 255
        # img = img[int(img.shape[0]/2):,:,1]
        _,prev_img = cv.threshold(img,low,255,cv.THRESH_OTSU)
        cv.imshow("Edge",prev_img)

    while cap.grab():
        _,img = cap.read()
        # img = cv.cvtColor(img[int(img.shape[0]/2):,:],cv.COLOR_BGR2GRAY)
        low = cv.getTrackbarPos("low threshold","Edge")
        # img = img[int(img.shape[0]/2):,:,1]
        _,threshold = cv.threshold(img[int(img.shape[0]/2):,:,2],low,255,cv.THRESH_BINARY)
        cv.imshow("Edge",cv.bitwise_and(prev_img,threshold,mask=prev_img))
        prev_img = threshold
        time.sleep(0.2)
        if cv.waitKey(1) == ord("q") :
            cycle = False
            cap.release()
            cv.destroyAllWindows()
            break
    cap.release()


    cap.release()
    cv.destroyAllWindows()