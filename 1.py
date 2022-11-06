import cv2
import numpy as np
# Choose the colors you want to detect
# lower and upper bounds for each color (HSV)
lower1 = {'red': (166, 84, 141), 'green': (66, 122, 129), 'blue': (97, 100, 117), 'yellow': (23, 59, 119), 'orange': (0, 50, 80)} 
upper1 = {'red': (186, 255, 255), 'green': (86, 255, 255), 'blue': (117, 255, 255), 'yellow': (54, 255, 255), 'orange': (20, 255, 255)}
sound=False
# initialize capture device
camera = cv2.VideoCapture('Tsunami_MH.mp4')

# define range of colors in HSV
colors = {'red': (166, 84, 141), 'green': (66, 122, 129), 'blue': (97, 100, 117), 'yellow': (23, 59, 119), 'orange': (0, 50, 80)} 

# color detection loop
while True:
    # get current frame
    try:
        (grabbed, frame) = camera.read()
        
        # convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow("Main Frame",frame)
        # for each color in colors
        numpy_vertical = []
        for key, value in colors.items():
            # create NumPy arrays from the boundaries

            lower = np.array(list(lower1[key]))
            upper = np.array(list(upper1[key]))
            # find the colors within the specified boundaries
            
            mask = cv2.inRange(hsv, lower, upper)
            yellow_lower=lower1["yellow"]
            yellow_upper=upper1["yellow"]
            yellow_mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
            yellow=cv2.bitwise_and(frame,frame,mask=yellow_mask)
            yellow_ratio=(cv2.countNonZero(yellow_mask))/(frame.size/7)
            if(yellow_ratio>0.30):
                print("Tsunami Alert")
            # show the images
            cv2.imshow(key + ' mask', mask)
        
        # if the 'q' key is pressed, stop the loop
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    except:
        pass
# cleanup
camera.release()
cv2.destroyAllWindows()