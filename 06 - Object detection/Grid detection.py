import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess = cv2.imread("chess.PNG")
plt.imshow(flat_chess)
#plt.show()

found,corners = cv2.findChessboardCorners(flat_chess,(7,7))

#plt.imshow(corners)
#plt.show()

print(cv2.drawChessboardCorners(flat_chess,(7,7),corners,found))
plt.imshow(flat_chess)
#plt.show()

# another pic

dots = cv2.imread("dots.PNG")
plt.imshow(dots)
#plt.show()
found,corners = cv2.findCirclesGrid(dots,(18,18),cv2.CALIB_CB_SYMMETRIC_GRID)

cv2.drawChessboardCorners(dots,(18,18),corners,found)
plt.imshow(dots)
plt.show()


#print(found)
#print(corners)