import numpy as np
import cv2
#rom video_write import VideoRecord
cam1 = cv2.VideoCapture("rtsp://admin:xiphos@123@192.168.1.9:554/mpeg/ch1/sub/av_stream")
cam2 = cv2.VideoCapture("rtsp://admin:xiphos@123@192.168.1.9:554/mpeg/ch2/sub/av_stream")
cam3 = cv2.VideoCapture("rtsp://admin:xiphos@123@192.168.1.9:554/mpeg/ch3/sub/av_stream")
cam4 = cv2.VideoCapture("rtsp://admin:xiphos@123@192.168.1.9:554/mpeg/ch4/sub/av_stream")
var_array=[]
path='D:\\Avik\\yolov4-deepsort\\data\\input\\'
size = (704,576)
#no_of_vars=2300
result = cv2.VideoWriter(path+'cctv_take_1.mp4',cv2.VideoWriter_fourcc(*'XVID'),10, size)
count=0
while(True):
    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()
    ret3, frame3 = cam3.read()
    ret4, frame4 = cam4.read()
    if ret1==True and ret2==True and ret3==True and ret4==True:
        hor1 = cv2.hconcat([frame1,frame2*0])
        hor2 = cv2.hconcat([frame3,frame4])

        var = cv2.vconcat([hor1,hor2])

        cv2.imshow('var', var)
        result.write(var)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else:
        break


cam1.release()
cam2.release()
cam3.release()
cam4.release()

result.release()
cv2.destroyAllWindows()
