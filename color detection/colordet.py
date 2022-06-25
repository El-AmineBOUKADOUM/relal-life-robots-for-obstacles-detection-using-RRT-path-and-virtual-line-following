import numpy as np
import cv2 

cap = cv2.VideoCapture(0)
centers = []
while True:
    ret, frame = cap.read()
    img = frame
    #orange
    
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    mas = cv2.inRange(hsv_img, (5,50,50), (15,255,255))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('ODDriginal',gray) 
    ret, thresh = cv2.threshold(gray, 20, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    H,W = img.shape[:2]
    AREA = H*W
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if not AREA/100<area<AREA/20:
            continue
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box,dtype="int")
        cv2.drawContours(img, [box], -1,(255,0,255) , 2, cv2.LINE_AA)
        M = cv2.moments(cnt)
        if M["m00"]>0 :
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centers[0]= (cX,cY)
            cv2.putText(img,'orange',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)   
        
        
    #BLUE
    
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    mas = cv2.inRange(hsv_img, (94, 80, 2), (126, 255, 255))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('ODDriginal',gray) 
    ret, thresh = cv2.threshold(gray, 20, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    H,W = img.shape[:2]
    AREA = H*W
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if not AREA/100<area<AREA/20:
            continue
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box,dtype="int")
        cv2.drawContours(img, [box], -1,(255,0,255) , 2, cv2.LINE_AA)
        M = cv2.moments(cnt)
        if M["m00"]>0 :
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(img,'blue',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)
            centers[1]= (cX,cY)
            
            
        

    #LIGHT GREEN
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    mas = cv2.inRange(hsv_img, (36,0,0), (86,255,255))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('ODDriginal',gray) 
    ret, thresh = cv2.threshold(gray, 20, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    H,W = img.shape[:2]
    AREA = H*W
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if not AREA/100<area<AREA/20:
            continue
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box,dtype="int")
        cv2.drawContours(img, [box], -1,(255,0,255) , 2, cv2.LINE_AA)
        M = cv2.moments(cnt)
        if M["m00"]>0 :
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            centers[2]= (cX,cY)
            cv2.putText(img,'light_green',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)
        
    print ('C = \n',centers)
    cv2.imshow('frame', img)
    if cv2.waitKey(0) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
