import cv2 as cv
from cv2 import VideoCapture
class CD:
    video = VideoCapture(0)
    while True:
        _, frame = video.read(0)
        #cv.imshow('frame', frame)
        #result = frame.copy()
        # Remove noise from the image
        blurred = cv.GaussianBlur(frame,(15,15),0)
        img_gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)  
        #thresh = 255-thresh #The function findContours describes the contour of areas consisting of ones. The areas in which you are interested are black, though.
        #if this is ACTIVATED means the objects are BLACK and the environment is WHITE [UP]
        #if this is DESACTIVATED means the objects are WHITE and the environment is BLACK [UP]

        contours, _  = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        #____________________________
        #Straight Bounding Rectangl
        # Get the bounding rectangle
        
        print("Number of Contours Returned: {}".format(len(contours)))
        clength=format(len(contours))
        clength=int(clength)
        contour = contours[:]
        yellowCL=[]
        ss=0
        '''
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            # Draw the rectangle around the object.
            #green=cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            #print (green)
            
            f=190
            xy=x-f
            yy=y-f
            wy=w+f
            hy=h+f
            yellow = cv.rectangle(frame, (xy, yy), (x+wy, y+hy), (0, 255, 255), 3)
            #print (yellow)
            
            yellowContour=([xy, yy],[x+wy, y+hy])
            print("\n yellowContour = ",yellowContour)                  
            
            yellowCL.insert(ss, yellowContour)
            print("yellowCL = ",yellowCL)
            ss += 1

        '''

        #____________________________
        #cv.drawContours(result, contours[:], -1, (0, 255, 0), 5)
        #print("Number of Contours Returned: {}".format(len(contours)))
        
        #____________________________
        #store the coutours on a list
        

            

        #result = cv.resize(result, (484, 640))
        #thresh = cv.resize(thresh, (484, 640))
        frameshape=frame.shape
        print(frameshape)
        cv.imshow("Shapes", frame)    
        cv.imshow("THRESH", thresh)
        key=cv.waitKey(0)
        if key==0 & 0xFF == ord('q'):
            break
    video.release(0)
