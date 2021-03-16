import cv2
import xml.etree.ElementTree as ET
import os
import glob

path = r"C:\Users\BHASKAR\Desktop\xml to txt\all"
store = r"C:\Users\BHASKAR\Desktop\xml to txt\new"
xml_paths = [str(img_path) for img_path in glob.glob(os.path.join(path, '*.xml'))]

for xml in xml_paths:
    img = xml.replace(".xml",".jpg")
    txt = xml.replace('.xml','.txt')
    print(img)
    image = cv2.imread(img)
    cv2.imwrite(img.replace(path,store),image)
    tree = ET.parse(xml)
    root = tree.getroot()
    classes = root.findall('object/name')
    classes = [item.text for item in classes]
    box = root.findall('object/bndbox')
    for i,item in enumerate(box):
        x1 = item[0].text
        y1 = item[1].text
        x2 = item[2].text
        y2 = item[3].text
        with open(txt.replace(path,store),"a+") as f:
            f.write(f"{classes[i]} {x1} {y1} {x2} {y2}\n")

print("Complete!!!")
