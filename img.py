import cv2
import time
cpt = 1 #start here for numbering of each pic
maxFrames = 50 # 200 is recommended

cap=cv2.VideoCapture(0)
time.sleep(10) #optional time to prepare for pic taking

#modify cv2.imwrite line below according to the image name and location

while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow("test window", frame) # show image in window
    cv2.imwrite("/home/bryan/tflite-custom-object-bookworm-main/images/rubikscube_%d.jpg" %cpt, frame)
    #cv2.imwrite('/home/bryan/tflite-custom-object-bookworm-main/images/clownfish_%d.jpg' %cpt, frame)
    time.sleep(1) #adjust as needed if more or less time needed between pics
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
