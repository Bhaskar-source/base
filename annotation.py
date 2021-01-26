import os
import glob
import cv2
import numpy as np
from tqdm import tqdm

'''
Raw annotation in format [ClassName Xmin Ymin Xmax Ymax]
Keep all the raw annotation images,texts and classes.txt in a particular folder and pass the location in root
Make another folder where all the images and YOLO format annotations will store and pass the location in store  
'''


def convert(image, coords):
    coords[2] -= coords[0]
    coords[3] -= coords[1]
    x_diff = int(coords[2] / 2)
    y_diff = int(coords[3] / 2)
    coords[0] = coords[0] + x_diff
    coords[1] = coords[1] + y_diff
    coords[0] /= int(image.shape[1])
    coords[1] /= int(image.shape[0])
    coords[2] /= int(image.shape[1])
    coords[3] /= int(image.shape[0])
    return coords


root = "D:\\project_data\\image"
store = "D:\\project_data\\annotation"
classes = {}
with open(os.path.join(root, "classes.txt"), "r") as myFile:
    for num, line in enumerate(myFile, 0):
        line = line.rstrip("\n")
        classes[line] = num
    myFile.close()
print(classes)

img_paths = [str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

for img in tqdm(img_paths):
    txt = img.replace(".jpg", ".txt")
    image = cv2.imread(img)
    annotation = list()
    try:
        with open(txt, "r") as file:
            for line in file:
                labels = line.split()
                labels[0] = classes.get(labels[0])
                coords = [float(i) for i in labels[1:]]
                labels[1:] = convert(image, np.asarray(coords))
                labels = [str(value) for value in labels]
                annotation.append(" ".join(labels))
            file.close()

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        pass
    cv2.imwrite(img.replace(root, store), image)
    with open(txt.replace(root, store), "w") as outfile:
        for line in annotation:
            outfile.write(line)
            outfile.write("\n")
        outfile.close()
