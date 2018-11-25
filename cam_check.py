import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    
    # Read the video frame
    ret, im =cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2. imshow('maut', im)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

if ret:
    print("camera is working")
else:
    print("Camera error! Try reconnecting")
