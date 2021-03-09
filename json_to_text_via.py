import json
import cv2
import os
json_file = r"D:\project\json_read_ITE\avik_part_2.json"
image_dir = r"D:\project\json_read_ITE\Avik_part_2"

with open(json_file,"r") as j:
    data = json.load(j)

for i in data:
    file = data.get(i)
    filename = file.get("filename")
    img = os.path.join(image_dir,filename)
    text = img.replace(".jpg",".txt")
    regions = file.get("regions")
    if len(regions)>=1:
        print(filename)
        for region_d in regions:
            shape = region_d.get("shape_attributes")
            coor = f"{shape.get('x')} {shape.get('y')} {shape.get('width')+shape.get('x')} {shape.get('height')+shape.get('y')}"
            region = region_d.get("region_attributes")
            for k in region:
                if region[k]:
                    coor = f"{k}:{region[k]} {coor}\n"
            with open(text,"a+") as f:
                f.write(coor)
    else:
        print(filename,"blank")