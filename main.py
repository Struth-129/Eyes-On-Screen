import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(grey,frame):
    face = face_cascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,5,5),2)
        r_grey = grey[y:y+h,x:x+w]
        r_frame = frame[y:y+h,x:x+w]
        eyes = eyes_cascade.detectMultiScale(r_grey,1.1,3)
        print(eyes)
        if isinstance(eyes,tuple) is False:
            cv2.putText(frame,"Focused",(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
        else:
            cv2.putText(frame,"Not-Focused",(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)  
    return frame         


cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    grey = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    output = detect(grey,frame)
    cv2.namedWindow('Detection',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Detection',1600,700)
    cv2.imshow('Detection',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
