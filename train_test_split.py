from sklearn.model_selection import train_test_split
import os
import glob
import shutil

root=r"C:\Users\BHASKAR\Desktop\face_forehead\all_yolo"
store = r"C:\Users\BHASKAR\Desktop\face_forehead"

train_path = os.path.join(store,"obj")
test_path  = os.path.join(store,"test")
os.mkdir(train_path)
os.mkdir(test_path)

img_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.jpg'))]

train,test = train_test_split(img_paths,test_size=.30)

for img in train:
    txt = img.replace(".jpg",".txt")
    print("[Train]",img)
    try:
        shutil.copy(img,img.replace(root,train_path))
        shutil.copy(txt,txt.replace(root,train_path))
    except:
        pass
print("\n")
for img in test:
    txt = img.replace(".jpg",".txt")
    print("[Test]",img)
    try:
        shutil.copy(img,img.replace(root,test_path))
        shutil.copy(txt,txt.replace(root,test_path))
    except:
        pass

print(f"\nTrain images: {len(train)} \nTest images: {len(test)}")



