import os
import cv2
import glob

root="D:\\vv"
store = "D:\\done_2"


img_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

for img in img_paths:
    frame = cv2.imread(img) 
    sav = img.replace(root,store)  
    cv2.imwrite(sav,cv2.resize(frame,(230,230)))
