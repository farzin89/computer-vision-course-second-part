
# detect the car plate

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('car.PNG')
def display(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    new_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)

display(img)
#plt.show()

# load the haarcascade_russian_plate_number_xml file.

plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# create a function that takes in an image and draw a rectangle around what to be a licence plate.
# keep in mind we're just deawing a tectangular around it for now,later on we'll adjust this function to blur.
# you may want to play with the scaleFactor and minNeighbor numbers to get good results.

def detect_plate(img):
    plate_img = img.copy()

    plate_rects = plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)

    for(x,y,w,h) in plate_rects:
        cv2.rectangle(plate_img,(x,y),(x+w,y+h),(0,0,255),4)
        return plate_img

result = detect_plate(img)
display(result)
#plt.show()

# Final Task : Edit the function so that is effectively blurs the detected plate,
# instead of just drawing a rectangle around it. Here are the steps you might want to take:

# 1- The hardest part is converting the (x,y,w,h) information into the dimension values you need
# grab an ROI (something we covered in the lecture 01- Blending and passing images. it's
# simply Numpy Slicing, you just need to convert the information about the top left corner of
# the tectangular and width and hight, into indexing position values.

# 2- once you've grabbed the ROI using the (x,y,w,h) values returned, you'll want to blur ROI.
# you can use cv2.mediaBlur for this.

# 3- Now that you have a blurred version of the ROI (the license plate) you will want to
#paste this blurred image back on to the original image at the same original location.
#simply using Numpy indexing and slicing to ressign that area of the original image to the blurred roi.

def detect_and_blur_plate(img):

    plate_img = img.copy()
    roi = img.copy()

    plate_rects = plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)

    for (x,y,w,h) in plate_rects:

        roi = roi[y:y+h,x:x+w]
        blurred_roi = cv2.medianBlur(roi,9)

        plate_img[y:y+h,x:x+w] = blurred_roi

    return plate_img

result = detect_and_blur_plate(img)
display(result)
plt.show()
