
""" Contours are defined as imply a curve joining all the continuous points(along
the boundary ), having same color or intensity.
Contours are a useful tool for shape analysis and object detection and recognition"""

""" Open CV has a built in Counter finder function that can also helps us differentiate between internal and external 
contours."""

import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('math.PNG')
print(img.shape)
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(img,cmap="gray")
thresh = 100

ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(img.shape)


for i in range (len(contours)):

  # External contour
  if hierarchy[0][i][3] == -1:

      cv2.drawContours(external_contours,contours,i,255,-1)

plt.imshow(external_contours,cmap='gray')
#plt.show()



# Internal
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh_img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

internal_contours = np.zeros(img.shape)


for i in range (len(contours)):

  # internal  contour
  if hierarchy[0][i][3] != -1:

      cv2.drawContours(internal_contours,contours,i,255,-1)

plt.imshow(internal_contours,cmap='gray')
plt.show()