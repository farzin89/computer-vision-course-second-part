
"""Template Matching is the simplest form of object detection .
it simply scans a larger image for a provided template by sliding the template target
image across the larger image.
the main that can be adjusted is the comparise method used as the target template is across
the larger image.
the methods are all some sort of correlation based metric."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

full = cv2.imread('farzin2.jpg')
full = cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
plt.imshow(full)
#plt.show()
print(full.shape)

face = cv2.imread('face.PNG')
face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
plt.imshow(face)
#plt.show()
print(face.shape)

"""All the 6 methods for comparison in a list
# Note how we are using strings,later on we'll use the eval() function to convert to function"""

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR','cv2.TM_CORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for m in methods:
        #CREATE A COPY
        full_copy = full.copy()

        method = eval(m)

        # template matching

        res = cv2.matchTemplate(full_copy,face,method)

        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc #(x,y)

        else :
            top_left = max_loc
        height,width,channels = face.shape

        bottom_right = (top_left[0] + width,top_left[1] + height )

        cv2.rectangle(full_copy,top_left,bottom_right,(255,0,0),10)

        # plot and show the images
        plt.subplot(121)
        plt.imshow(res)
        plt.title('HEATMAP OF TEMPLATE MATCHING')
        plt.show()

        plt.subplot(122)
        plt.imshow(full_copy)
        plt.title ('DETECTION OF TEMPLATE')
        # tittle with the method used
        plt.suptitle(m)
        plt.show()

        print('\n')
        print('\n')