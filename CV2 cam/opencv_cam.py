import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    start_time = time.time()
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(1.0 - time.time() + start_time) # Sleep for 1 second minus elapsed time

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()