import cv2
import os

Face_Cascade = cv2.CascadeClassifier(r"D:\Final_Year_Project_Dataset\Code_Files\haarcascade_frontalface_default.xml")

def changer(img):
    grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=Face_Cascade.detectMultiScale(grey, 1.3, 6)
    for (x, y, w, h) in faces:
        sub_colour=img[y:y+h, x:x+w]
        img=sub_colour

    img = cv2.resize(img, (100, 100))
    return img

folder = r"D:\Final_Year_Project_Dataset\Pictures"

for dirs in os.listdir(folder):
    new_path = os.path.join(r"D:\Final_Year_Project_Dataset\Pictures_Edited", dirs)
    os.mkdir(new_path)
    for files in os.listdir(os.path.join(folder, dirs)):
        try:
            image_path = os.path.join(folder, dirs, files)
            img = cv2.imread(image_path)[:, :, ::-1]
            img = changer(img)
            cv2.imwrite(os.path.join(new_path, f"{files}.jpg"), img)
        except:
            print(dirs, " ---> ", files)