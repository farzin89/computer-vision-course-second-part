
import cv2
import numpy as np
import matplotlib.pyplot as plt

real_chess = cv2.imread('reall.PNG')
real_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)

flat_chess = cv2.imread('chess.PNG')
flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)

gray_flat_chess = cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
gray_reall_chess = cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray_flat_chess,65,0.01,10)
corners = np.int0(corners)

for i in corners :
    x,y = i.ravel()
    cv2.circle(flat_chess,(x,y),3,(255,0,0),-1)

plt.imshow(flat_chess)
#plt.show()

corners = cv2.goodFeaturesToTrack(gray_reall_chess,80,0.01,10)
corners = np.int0(corners)
for i in corners :
    x,y = i.ravel()
    cv2.circle(real_chess,(x,y),3,(255,0,0),-1)

plt.imshow(real_chess)
plt.show()


