import os
import cv2
import glob

root="C:\\Users\\BHASKAR\\Downloads\\TCG_Video_clips\\TCG_Video_clips"
store ="D:\\project_data\\TCG"

img_paths=[str(img_path) for img_path in glob.glob(os.path.join(root, '*.dav'))]

c=80000000
for video in img_paths:
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print("Cannot open camera",video)
        exit()
    while True:

        ret, img = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...",video)
            break
        big = cv2.resize(img, (800,800))
        cv2.imwrite(store+'\\TCG_'+str(c) + ".jpg", big)
        c+=1
        if cv2.waitKey(1) == ord('q'):
            cap.release()
            break

cv2.destroyAllWindows()