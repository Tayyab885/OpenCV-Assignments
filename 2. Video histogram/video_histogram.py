import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
vid = cv.VideoCapture("barriers.avi")
while True:
    ret, frame = vid.read()
    if ret == True: 
        cv.imshow("Video",frame)
        hist = cv.calcHist([frame],[0],None,[256],[0,256])
        plt.plot(hist)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    elif ret == False:
        vid = cv.VideoCapture("barriers.avi")
        ret, frame = vid.read()
        cv.imshow("Video",frame)
        hist = cv.calcHist([frame],[0],None,[256],[0,256])
        plt.plot(hist)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
plt.show()
vid.release()
cv.destroyAllWindows()