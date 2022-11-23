import numpy as np
import matplotlib.pyplot as plt
import cv2

cap1 = cv2.VideoCapture('barriers.avi')
cap2 = cv2.VideoCapture('barriers.avi')
fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(8, 4), sharey=True)
while cap1.isOpened() or cap2.isOpened():
    ret1  , frame1 = cap1.read()
    ret2 , frame2 = cap2.read()

    if ret1:
        hest1 = cv2.calcHist([frame1],[0],None,[256],[0,256])
        ax1.plot(hest1)
        cv2.imshow('Video1' , frame1)

    if ret2:
        hest2 = cv2.calcHist([frame2],[0],None,[256],[0,256])
        ax2.plot(hest2)
        cv2.imshow('Video2' , frame2)
    ## To Rerun Video From Start
    if not ret1 or not ret2:
        cap1 = cv2.VideoCapture('barriers.avi')
        cap2 = cv2.VideoCapture('barriers.avi')
        ret1  , frame1 = cap1.read()
        ret2 , frame2 = cap2.read()

        if ret1:
            hest1 = cv2.calcHist([frame1],[0],None,[256],[0,256])
            ax1.plot(hest1)
            cv2.imshow('Video1' , frame1)

        if ret2:
            hest2 = cv2.calcHist([frame2],[0],None,[256],[0,256])
            ax2.plot(hest2)
            cv2.imshow('Video2' , frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.waitKey(1)
plt.show()
cap1.release()
cap2.release()
cv2.destroyAllWindows()