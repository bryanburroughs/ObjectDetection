import cv2
from picamera2 import Picamera2
import time

#NOTE: Use this for Raspberry Pi cam. Does not work properly with USB camera.

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640,480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()
cpt = 1 #start here for numbering of each pic
maxFrames = 30

#modify cv2.imwrite line below according to the image name and location

while cpt < maxFrames:
    im= picam2.capture_array()
#    im=cv2.flip(im,-1) #flip image
    cv2.imshow("Camera", im)
    cv2.imwrite('/home/bryan/tflite-custom-object-bookworm-main/images/clownfish_%d.jpg' %cpt, im)
    time.sleep(0.5) #adjust as needed if more or less time needed between pics
    cpt += 1
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()
