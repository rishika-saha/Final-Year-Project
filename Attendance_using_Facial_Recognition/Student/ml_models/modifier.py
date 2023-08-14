import cv2

def changer(img_path):
    img=cv2.imread(img_path)
    img = cv2.flip(img, 1)
    grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Face_Cascade = cv2.CascadeClassifier(r"D:\Final_Year_Project_Dataset\Student\ml_models\haarcascade_frontalface_default.xml")
    faces=Face_Cascade.detectMultiScale(grey, 1.1, 5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        sub_grey=grey[y:y+h, x:x+w]

    sub_grey = cv2.resize(sub_grey, (100, 100))
    cv2.imwrite('D:\Final_Year_Project_Dataset\Student\Images_Folder\Img_1.jpg', sub_grey)