import cv2
import  numpy as np
import matplotlib.pyplot as plt

road = cv2.imread('bridge.PNG')
road_copy = np.copy(road)

#print(road.shape[:2])

marker_image = np.zeros(road.shape[:2],dtype=int)
segments = np.zeros(road.shape)
print(marker_image.shape)
print(segments.shape)

from matplotlib import cm
#print(cm.tab10(0))
def create_rgb(i):
   return tuple(np.array(cm.tab10(i)[:3])* 255)

colors = []
for i in range(10):
   colors.append(create_rgb(i))

#print(colors)

#Global variables
#Color choice
n_markers = 10 # 0-9
current_marker = 1
# Markers updated by watershed
marks_updated = False

#callBack Function
def mouse_callback (event,x,y,flags,parm):
    global marks_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(marker_image,(x,y),10,(current_marker),-1)

        # user sees on the Road image
        cv2.circle(road_copy,(x,y),10,colors[current_marker],-1)

        marks_updated = True

# While True
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image',mouse_callback)

while True:

    cv2.imshow('watershed Segments',segments)
    cv2.imshow('road Image',road_copy)

    # Close all windows
    k = cv2.waitKey(1)
    if k == 27:
        break
    # Crearing all the colors press c key
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2],dtype=int)
        segments = np.zeros(road.shape)

    #Update color choice
    elif k > 0 and chr(k).isdigit():
       current_marker = int(chr(k))

    # Update the marking
    if marks_updated :
        marker_image_copy = marker_image.copy()
        cv2.watershed(road,marker_image_copy)

        segments = np.zeros(road.shape)
        for color_ind in range (n_markers):
            # Coloring segments, numpy call
            segments[marker_image_copy == (color_ind)] = colors[color_ind]


cv2.destroyAllWindows()