
""" When thinking about corner detection in computer vision,we should ask ourselves:
  - what is a coener ?

 A corner is a point whose local neighborhood stands in two dominant and different edge directions.
 and A corner can be interpreted as the junction of two edges, where an edge is a sudden change in image brightness.
 """
""" there are various corner detection algorithms.
We will take a look at some of the most popular algorithms:
- Harris Corner Detection
_ shi-Tomasi Corner Detection"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread('chess.PNG')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)


gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_flat_chess,cmap='gray')
#plt.show()

real_chess = cv2.imread('reall.PNG')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)
#plt.show()

gray_reall_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_reall_chess,cmap='gray')
#plt.show()

gray = np.float32(gray_flat_chess)
dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)
flat_chess[dst > 0.01 * dst.max()] = [255,0,0] # RGB
plt.imshow(flat_chess)
#plt.show()

gray = np.float32(gray_reall_chess)
dst = cv2.cornerHarris(src= gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)
real_chess[dst > 0.01 * dst.max()] = [255,0,0]
plt.imshow(real_chess)
plt.show()


