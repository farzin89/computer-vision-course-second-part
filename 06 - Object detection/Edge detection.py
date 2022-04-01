
''' in this lecture we will learn how to use the Canny edge detector, one of the most popular
edge detection algorithms.'''

""""Canny Edge Detection Process

  - Apply Gaussian filter to smooth the image in order to remove the noise 
  - Find the intensity gradients of the image
  - Aplly non-maximum suppression to get rid of spurious response to edge detection 
  - Apply double threshold to determine potential edges
  - Track edge by hysteresis: Finalize the detection of edges by suppressing all the 
  other edges that are weak and not connected to strong edges."""

""" Note : For high resolution images where you only want general edges, it is usually a good idea 
to apply a custom blur before applying the Canny Algorithm"""

""" The Canny algorithm also requires user to decide on low and high threshold values."""

import cv2
import  numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('face.PNG')
plt.imshow(img)
#plt.show()

edges = cv2.Canny(image=img,threshold1=127,threshold2=127)
plt.imshow(edges)
#plt.show()

# first method for detecting the edge without noise is playing threshold
edges = cv2.Canny(image=img,threshold1=127,threshold2=127)
plt.imshow(edges)

# use formula that may help us for choossing the threshold

med_val = np.median(img)
print(med_val)

# set the lower threshold to either 0 or 70% of median value whichever is greater

lower = int(max(0,0.70 * med_val))
# upper threshold to either 130% of the median or the max 255 , whichever is smaller
upper = int(min(255,1.3 * med_val))

edges = cv2.Canny(image=img,threshold1=lower,threshold2=upper + 100)
plt.imshow(edges)
#plt.show()

# bluring that image

blurred_img = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(image=blurred_img,threshold1=lower,threshold2=upper + 50)
plt.imshow(edges)
plt.show()


