
import cv2
import numpy as np
import matplotlib.pyplot as plt

def display (img,cmap= 'gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

reeses = cv2.imread('reeses puffs.PNG',0)
display(reeses)
#plt.show()

cereals = cv2.imread('cereal.PNG',0)
display(cereals)
#plt.show()

orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(reeses,None)
kp2,des2 = orb.detectAndCompute(cereals,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
matches = bf.match(des1,des2)
#print(matches)
#print(len(matches))
matches = sorted(matches,key=lambda x:x.distance)
reeses_matches = cv2.drawMatches(reeses,kp1,cereals,kp2,matches[:25],None,flags=2)
display(reeses_matches)
plt.show()