
""" in geograghy, a watershed is a land area that chennels rainfall and snowmelt to
 creeks,streams,and rivers,and eventually to outflow poins such as reservoirs,bays,and
 the ocean
 these watersheds can then be segmented as topographical maps with boundaries.

 Metaphorically, the watershed algorithm transformation treats the image it operates
 upon like a topographic map, with the brightness of each point representing its height,
 and finds the lines that run along the tops of ridges.

  Any grayscale image can be viewed as a topographic surface where high intensity
  denotes peaks and hills while low intensity denotes valleys.

  The algorithm can then fill every isolated valleys (local minima) with different
  colored water (labels)

  as the " Water" rises, depending on the peaks(gradients) nearby,"water"
  from different valleys (different segments of the image), with different colors
  could start to merge.

  to avoid this merging, the algorithm creates barriers (segment edge boundaries) in
  location where "water" merges.

  This algorithm is especially usefull for segmenting images into background and foreground
  in situations that are difficult for other algorithms.

  A common example is the use of coins next to each other on a table."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(img,cmap ='gray'):
    fig = plt.figure(figsize=(12,10))
    ax  = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

sep_coins = cv2.imread('seo_coins.PNG')
display(sep_coins)
#plt.show()

# Median Blur
# Grayscale
#Binary threshold
#find contours

sep_blur = cv2.medianBlur(sep_coins,25)
display(sep_blur)
#plt.show()

gray_sep_coins = cv2.cvtColor(sep_blur,cv2.COLOR_BGR2GRAY)
display(gray_sep_coins)
#plt.show()

ret,sep_thresh = cv2.threshold(gray_sep_coins,160,255,cv2.THRESH_BINARY)
display(sep_thresh)
#plt.show()

contours,hierarchy = cv2.findContours(sep_thresh.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

external_contours = np.zeros(sep_coins.shape)


for i in range (len(contours)):

  # External contour
  if hierarchy[0][i][3] == -1:

      cv2.drawContours(sep_coins,contours,i,(255,0,0),10)

display(sep_coins)
plt.show()




