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

nadia = cv2.imread('Nadia.jpgad',0)
denis = cv2.imread('Denis.jpg',0)
solvay = cv2.imread('Solvay_conference2.jpg',0)

plt.imshow(solvay,cmap='gray')
