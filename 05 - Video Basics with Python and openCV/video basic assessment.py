import cv2

# Create a function based on a cv2 Event (left button click)


# mouse callback function
def draw_circle(event,x,y,flags,param):
    global center,clicked

    # get mouse click on down amd track center
    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False
    if event == cv2.EVENT_LBUTTONUP :
        clicked = True


    #use boolean variable to track if the mouse has been released




# Haven't drawn anything yet
center = (0,0)
clicked = False


# capture video
cap = cv2.VideoCapture(0)

# Create a named window for connections
cv2.namedWindow('test')

# Bind draw_circle function to mouse cliks
cv2.setMouseCallback('test',draw_circle)

while True:

    # Capture frame-by-frame
    ret,frame = cap.read()

    # use if statement to see if clicked is true
    if clicked :
        # Draw circle on fram
        cv2.circle(frame,center=center,radius=50,color=(255,0,0),thickness=5)

        # Display the resulting frame
    cv2.imshow('test',frame)

    # this command let's us quit with the "q" button on a keyboard.
    #simply pressing X on the window won't work
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# when everything is done,release the capture
cap.release()
cv2.destroyAllWindows()
