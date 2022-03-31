
import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# TOP LEFT CONNER
x = width // 2  # // the result will be integer
y = height//2

# width and height of RECTANGLE
w = width //4
h = height // 4

#BOTTOM RIGHT x + w,y + h

while True :

    ret,frame = cap.read()

    cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,0,255),thickness=5)

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()