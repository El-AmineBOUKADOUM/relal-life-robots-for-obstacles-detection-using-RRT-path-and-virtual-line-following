def red (img,centers):
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
     
    mas = cv2.inRange(hsv_img, (0,122,156), (180,188,255))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ODDriginal',gray) 
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
            centers [0] = (cX,cY)
            cv2.putText(img,'red',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)   
          
    return img, centers

def blue(img,centers):
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    mas = cv2.inRange(hsv_img, (61, 0, 89), (146, 116, 170))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ODDriginal',gray) 
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
            centers [1] = (cX,cY)
            cv2.putText(img,'blue',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)
          
          
    return img, centers

def green(img,centers):
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
     
    mas = cv2.inRange(hsv_img, (36,0,0), (86,255,255))
    
    blue=cv2.bitwise_and(img,img,mask=mas)
    gray = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ODDriginal',gray) 
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
            centers [2] = (cX,cY)
            cv2.putText(img,'green',(cX - 20, cY - 20), font, 1,(0,255,255),2,cv2.LINE_AA)
          
          
    return img, centers



import numpy as np
import cv2 



cap = cv2.VideoCapture('http://192.168.227.149:8080/video')

  
while True:
    
    ret, frame = cap.read()
    center = [(0,0),(0,0),(0,0)]
    img, centers = red(frame, center)
    img, centers = blue(frame, center)
    img, centers = green(frame, center)
    print('centers = ', centers)
    

    cv2.imshow('frame', img)
    if cv2.waitKey(0) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





from distutils.util import execute
import numpy as np
from numpy import pi
import pygame
import sched, time
import math
from math import atan2, pi

s = sched.scheduler(time.time, time.sleep)
t1=0
t1=time.time()
w = 1.2 #rad/s
dt = 0
KP,KI,KD = 0,0,0
integral,deriv = 0,0

background_colour = (255,255,255) # For the background color of your window
(width, height) = (720, 480) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('the man with the if') # Name for the window
screen.fill(background_colour) #This syntax fills the background colour



p1 = np.array(centers [0])
p2 = np.array(centers [2])
p3 = np.array(centers [1])  

point1= pygame.draw.circle(screen, (255, 0, 0), p1, 10, 0) #R
point2= pygame.draw.circle(screen, (0, 255, 0), p2,10, 0) #G
Point3= pygame.draw.circle(screen, (0, 0, 255), p3, 10, 0) #B

pygame.display.flip()


U = p1 - p2
V = p3 - p2

cosine_angle = np.dot(U,V) / (np.linalg.norm(U) * np.linalg.norm(V))
angle = np.arctan2(abs(np.cross(V, U)),np.dot(U, V))*360/(2*pi)
if (np.cross(V,U) > 0): angle = 360 - angle


while True:
    
    print(angle)
   

    if angle == 180:
            
        print ('move forward')
        time.sleep(2)
    elif angle < 180:
        print ('translate left')
        rotated=pygame.transform.rotozoom(red,math.degrees(angle),1)
        time.sleep(2)
    elif angle > 180:
        print ('translate right')
        time.sleep(2)
        
       




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()