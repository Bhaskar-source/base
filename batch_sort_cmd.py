import os
import cv2
import glob
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-r","--root",help="location of images")
parser.add_argument("-s","--store",help="location to save")
parser.add_argument("-b","--batch",help="Total images in single batch")
args = vars(parser.parse_args())

root = args["root"]
store = args["store"]
batch_size = int(args["batch"])

print("[INFO] Start..")
img_paths = [str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]
pic =len(img_paths)
end=batch_size
start=0
count=0
while (True):
    dir_pa = os.path.join(store, str(start) + "-" + str(end))
    os.mkdir(dir_pa)
    print(f"[INFO] Start BATCH NO. {end//batch_size}")
    for img in range(start, end):
        frame = cv2.imread(img_paths[img])
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)         # img operation
        cv2.imwrite(img_paths[img].replace(root,dir_pa),gray_frame)
        count+=1
        if count == pic:
            break
    if count == pic:
        break
    start += batch_size
    end += batch_size
