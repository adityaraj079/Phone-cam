import cv2
import numpy as np
url = 'rtsp://192.168.43.145'
cap = cv2.VideoCapture(url)
while (True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q=cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
