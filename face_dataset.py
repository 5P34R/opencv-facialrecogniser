import cv2
import numpy as np
import os

face_id = input("Enter your id: ")
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
print("intalizing webcam please focus on your camera")

count = 0
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.5, 5)
    #1
    #x,y,w,h = face
    for x,y,w,h, in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)
    try:
        path = os.getcwd()
        dirt = "Dataset"
        parent = os.path.join(path, dirt)
        os.mkdir(parent, 777)
        print("Dataset  directory is created in %s ",(parent))
    except Exception as e:
        continue
    if cv2.waitKey(1) == 27:
        break
    elif count == 30:
        break
cap.release
cv2.destroyAllWindows()