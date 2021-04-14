import cv2
import os
class Label:
    def __init__(self,frame:list,class_name:str,box:list):
        self.frame = frame
        self.class_name = class_name
        self.box = box

    def Xception(self,frame_no:int,name:str):
        self.frame_no = frame_no
        self.name     = name
        location = os.getcwd()
        folder = os.path.join(location,self.name)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        img = os.path.join(folder,f"{self.name}_{self.frame_no}.jpg")
        n = [abs(int(i)) for i in self.box]
        xmin, ymin, xmax, ymax = n
        frame = self.frame[ymin:ymax,xmin:xmax]
        cv2.imwrite(img, frame)
        print(f"[INFO] : Cropping Image")

    def Yolo(self,frame_no:int,name:str):
        self.frame_no = frame_no
        self.name = name
        location = os.getcwd()
        folder = os.path.join(location, self.name)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        img = os.path.join(folder, f"{self.name}_{self.frame_no}.jpg")
        if not os.path.isfile(img):
            cv2.imwrite(img,self.frame)
        n = [abs(int(i)) for i in self.box]
        xmin, ymin, xmax, ymax = n
        with open(img.replace(".jpg",".txt"),"a+") as f:
            f.write(f"{self.class_name} {xmin} {ymin} {xmax} {ymax}\n")
        print(f"[INFO] : LabelIng Image")    
