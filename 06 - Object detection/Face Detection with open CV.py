""" in thids lecture we will explore face detection using Haar Cascades, which is key component
of the Viola-Jones object detection frmework.
Keep in mind, this is face Detection Not face recognition.
we will be able to very quickly detect if a face is in an image and locate it.
However we won't know who's face it belongs to.
We would need a really large dataset and deep learning for facisl recognition.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

nadia = cv2.imread('nadia.PNG',0)
denis = cv2.imread('Denis.jpg',0)
solvay = cv2.imread('Solvay_conference2.jpg',0)

#plt.imshow(nadia,cmap='gray')
#plt.show()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face (img):

     face_img = img.copy()
     face_rects = face_cascade.detectMultiScale(face_img)

     for (x,y,w,h) in face_rects:
         cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)

     return face_img

result = detect_face(solvay)
#plt.imshow(result,cmap = 'gray')
#plt.show()
# sometime detect wrongly in picture which has many people
# in order to solve that we are going to add few parameters

def adj_detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)

    return face_img
#result = adj_detect_face(solvay)
#plt.imshow(result,cmap = 'gray')
plt.show()

# eye detection

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


def detect_eyes(img):

    face_img = img.copy()
    eyes_rects = eye_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)

    for (x, y, w, h) in eyes_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)

    return face_img

result = detect_eyes(nadia)
#plt.imshow(result,cmap = 'gray')
#plt.show()

# detect from camera

cap = cv2.VideoCapture(0)

while True :

    ret,frame = cap.read(0)

    frame = detect_face(frame)

    cv2.imshow('video face detect',frame)

    k = cv2.waitKey(1)
    if k== 27:
        break

cap.release()
cv2.destroyAllWindows()


