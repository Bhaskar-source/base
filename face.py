import numpy as np
import pandas as pd
import os
import glob
import cv2

corr = lambda x: x - 5

l = []


def click_event(event, x, y, flags, params):
    global l
    global c

    if event == cv2.EVENT_LBUTTONDOWN:  # For left click
        l.append((corr(x), y))
        print(l)
        if len(l) == 2:
            x1,y1 = l[0]
            x2,y2 = l[1]
            cv2.imshow('image', im)
            image = im[y1:y2,x1:x2]
            cv2.imwrite("D:\\Data\\TO_DONE\\done_" + str(c) + ".jpg", image)
            c += 1
            cv2.waitKey(1)

    if event == cv2.EVENT_RBUTTONDOWN:  # For right click

        cv2.imshow('image', im)
        cv2.waitKey(1)


#######################################################################################

root = "D:\\Data\\TO_WORK"  # make a directory which contains folder name "images" & "texts"

# images = os.path.join(root,"images")

img_paths = [str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

c = 1000
for img in img_paths:

    im = cv2.imread(img)
    cv2.imshow('image', im)
    cv2.setMouseCallback('image', click_event)
    l = []
    # cv2.imwrite("no_done"+str(c)+".jpg",im)

    if cv2.waitKey(0) & 0xFF == ord('s'):
        break
    cv2.destroyAllWindows()

