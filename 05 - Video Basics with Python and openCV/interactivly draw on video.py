
import cv2



# Call back function rectangle
def draw_rectangle (event,x,y,flags,param):

    global pt1,pt2,topLeft_clicked,botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # Reset the rectangle (it checks if the rect there)
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True

        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True


# Global variables
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

# connect to the callback
cap = cv2.VideoCapture(0)

cv2.namedWindow('test')
cv2.setMouseCallback('test',draw_rectangle)
while True :

    ret,frame = cap.read()

    #Drawing on the Frame mased off the global variables
    if topLeft_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)

    if topLeft_clicked and botRight_clicked :
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv2.imshow("test",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()