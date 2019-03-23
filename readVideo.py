import cv2
import numpy as cv

#/Users/shishirumesh/Github/Semantic-Segmentation-TransAI/video/video1.mp4

#Reads the video file from the system
cap = cv2.VideoCapture('/Users/shishirumesh/Github/Semantic-Segmentation-TransAI/video/video2.mp4')
#Creates a codec to write the video file to a file after modifications
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#Specifies the parameters of the outpur video
video = cv2.VideoWriter('vid-mod.avi',fourcc,cap.get(cv2.CAP_PROP_FPS),(int(cap.get(3)), int(cap.get(4))))

#Runs the loop till frames are available
while True:
    #Reads the frame
    ret, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.line(img, (0,0),(150,150), (255,255,255),15)
    cv2.imshow('video output',img)
    video.write(img)
    if(cv2.waitKey(1) and 0xFF == ord('q')):
        break

cap.release()
video.release()
cv2.destroyAllWindows()
