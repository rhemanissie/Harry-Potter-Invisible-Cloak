import cv2 as cv
import numpy as np
import time


cap = cv.VideoCapture(0) ## capture live feed from the web cam

fourcc = cv.VideoWriter_fourcc(*'XVID') ## 
out = cv.VideoWriter('invisibility cloak.avi',fourcc,20.0,(640,480))   ##contains the feed from the web cam , save the feed in the video format, inputs --> frame rate and resolution


time.sleep(2) ## this is the hault or the delay after the cam is on it is not stable the delay makes it stable



background = 0
for i in range(30):
    ret, background = cap.read()  ## captures background and stores img and information

while (cap.isOpened()): ## this is performed  when the person with the cloak appears 
    ret, img = cap.read() ## reads the image 

    if not ret:
        break


    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV) 


    # hsv values
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask1 = cv.inRange(hsv,lower_red,upper_red)

    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])

    mask2 = cv.inRange(hsv,lower_red,upper_red)  


    mask1 = mask1 + mask2 ## this is bitwise or not addition
    mask1 = cv.morphologyEx(mask1, cv.MORPH_OPEN, np.ones((3,3), np.uint8),iterations=2)
    mask2 = cv.morphologyEx(mask1, cv.MORPH_DILATE, np.ones((3,3), np.uint8),iterations=1)

    mask2 = cv.bitwise_not(mask1)

    res1 = cv.bitwise_and(background,background,mask = mask1)
    res2 = cv.bitwise_and(img,img,mask = mask2)

    final_output = cv.addWeighted(res1,1,res2,1,0)

    cv.imshow('Cloak Project', final_output)
    k = cv.waitKey(10)
    if(k == 27):
        break


cap.release()
cv.destroyAllWindows()
