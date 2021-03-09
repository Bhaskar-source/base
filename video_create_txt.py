import cv2
import os
import glob
import random
root = r"D:\project\json_read_ITE\Kuntal_part_2\K_7403-7650"
img_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.png'))]

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
result = cv2.VideoWriter('part2\ITE_KUNTAL_1.AVI', cv2.VideoWriter_fourcc(*'MJPG'), 20, (800,800))

d = [["IDENTIFICATION","STEP IDENTIFICATION"],['REMOVAL',"STEP REMOVAL"],["ACTION","STEP ACTION"]]
k = []
for img in img_paths:
    frame = cv2.imread(img)
    #txt = img.replace(".jpg",".txt")
    #print(img)
    try:
        #print("1")
        with open(txt,"r") as f:
            print("2")
            for line in f:
                #print("3")
                line = line.rstrip("\n")
                line = line.split(" ")
                class_id = line[0]
                x1 = int(line[1])
                y1 = int(line[2])
                x2 = int(line[3])
                y2 = int(line[4])
                x1 = random.randint(x1-5,x1+5)
                x2 = random.randint(x2-5,x2+5)
                y1 = random.randint(y1-5,y1+5)
                y2 = random.randint(y2-5,y2+5)
                t = class_id.split(":")
                print(t)
                frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255), 2)
                frame = cv2.putText(frame, t[1], (x1,y1-10), font, 1, (0,255,0),2)


                if t[0] in d[0][0]:
                    frame = cv2.putText(frame, d[0][1], (50, 80), font, .8, (0, 255, 0), 2)  # Fixed
                elif t[0] in d[1][0]:
                    frame = cv2.putText(frame, d[1][1], (50, 105), font, .8, (0, 255, 0), 2)  # Fixed
                elif t[0] in d[2][0]:
                    frame = cv2.putText(frame, d[2][1], (50, 80), font, .8, (0, 255, 0), 2)

    except:
        print("ex")
        pass
    #frame = cv2.putText(frame, "IDENTIFY DEFECTS", (50, 50), font, 1, (0, 255, 0), 2)  # Fixed
    result.write(frame)
    #cv2.imshow("img", frame)
    #cv2.waitKey(1)


result.release()
cv2.destroyAllWindows()
