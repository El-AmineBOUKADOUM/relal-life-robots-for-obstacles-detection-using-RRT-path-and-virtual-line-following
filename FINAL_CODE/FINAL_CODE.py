from distutils.util import execute
from simple_pid import PID
import numpy as np
from numpy import pi
import pygame
import sched, time
import math
from math import atan2, pi
import os
import numpy as np
import cv2 

import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap

from sys import exit
import time


def rrt_planning():
    map_path = 'enter YOUR map path here'
    start=(50,50)
    goal=(700,500)
    iteration=0
    t1=0
    

    pygame.init()
    map=RRTMap(start,goal,map_path)
    graph=RRTGraph(start,goal,(map.mapw,map.maph))
    
    map.drawMap()
    t1=time.time()

    while (not graph.path_to_goal()):
  #      print('time',t1)

        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        #raise exception if timeout
        if elapsed > 20:
            print('timeout re-initiating the calculations')
            raise

        if iteration % 100 == 0:
            X, Y, Parent = graph.bias(goal,map.original_map)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)

        else:
            X, Y, Parent = graph.expand(map.original_map)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)

        if iteration % 5 == 0:
            pygame.display.update()
        iteration += 1
        
    
    map.drawPath(graph.getPathCoords())
    
    pygame.display.update()
    pygame.image.save(map.map,'ourMap.jpeg')
    return map.map, graph.getPathCoords()
    



def red (img,centers):
    hsv_img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    font = cv2.FONT_HERSHEY_SIMPLEX
         
    mas = cv2.inRange(hsv_img, (0,100,255), (36,255,255))
    
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
    
    mas = cv2.inRange(hsv_img, (94, 80, 2), (126, 255, 255))
    
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
     
    mas = cv2.inRange(hsv_img, (40, 40,40), (70, 255,255))
    
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






#cap = cv2.VideoCapture('http://192.168.227.149:8080/video')
img = cv2.imread(r'C:\Users\acer\Desktop\test2.png')
while True:
    frame = img
    #ret, frame = cap.read()
    center = [(0,0),(0,0),(0,0)]
    img, centers = red(frame, center)
    img, centers = blue(frame, center)
    img, centers = green(frame, center)
    print('centers = ', centers)
    

    cv2.imshow('frame', img)
    if cv2.waitKey(0) == ord('q' or 'Q'):
        break
#cap.release()
cv2.destroyAllWindows()



s = sched.scheduler(time.time, time.sleep)
t1=0
t1=time.time()
w = 1.2 #rad/s
#dt = 0
KP,KI,KD = 0,0,0
integral,deriv = 0,0

background_colour = (255,255,255) # For the background color of your window
(width, height) = (720, 480) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('the man with the if') # Name for the window
screen.fill(background_colour) #This syntax fills the background colour


#robot points
p1 = np.array(centers [0]) #R
p2 = np.array(centers [2]) #G

# waypoint
p3 = np.array(centers [1]) #B

point1= pygame.draw.circle(screen, (255, 0, 0), p1, 10, 0) #R
point2= pygame.draw.circle(screen, (0, 255, 0), p2,10, 0) #G
Point3= pygame.draw.circle(screen, (0, 0, 255), p3, 10, 0) #B

#tests were here
pygame.display.flip()




def desired_angle(points):
    p1,p2,p3 = points
    U = p1 - p2
    #TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
    V = p3 - p2
    angle = np.arctan2(abs(np.cross(V, U)),np.dot(U, V))*360/(2*pi)
    if (np.cross(V,U) > 0): angle = 360 - angle
    #angle = 360 -angle
    return angle
angle = desired_angle((p1,p2,p3))

class Envir:
    def __init__(self,dimention):
        #colors
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0 ,255,0)
        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.yel = (255,255,0)
        #map dimension
        self.height=dimention[0]
        self.width=dimention[1]
        #window setting
        pygame.display.set_caption("RRT-MASTERS")
        self.map=pygame.display.set_mode((self.width,self.height))

        ##self.font=pygame.font.Font('freesansbold.ttf',50)
        #self.text=self.font.render('default',True,(0,0,0),(255,255,255))
        #self.textRect=self.text.get_rect()
        #self.textRect.center=((720-600),(480-100))

    def draw_robot(self,robot_center,robot_front):
        xr = robot_front[0]
        yr = robot_front[1]
        pygame.draw.circle(self.map, self.green, robot_center, 10, 0)
        pygame.draw.circle(self.map, self.red, (int(xr),int(yr)), 10, 0)
    
    def draw_path(self,waypoints):
        for wp in waypoints:
            pygame.draw.circle(self.map, self.blue, (int(wp[0]),int(wp[1])), 5, 0)


    def write_info(self,Vl,Vr,theta):
        txt=f"Vl = {Vl} Vr = {Vr} theta = {int(math.degrees(theta))}"
        self.text=self.font.render(txt,True,(0,0,0),(255,255,255))
        self.map.blit(self.text,self.textRect)

class Robot:
    def __init__(self,P,ANGLE,path):
        self.m2p=3779.52
        self.targets = path
        self.waypoint = 0
        self.w = 0.01
        self.x=self.targets[0][0]
        print('x == ', self.x)
        self.y=self.targets[0][1]
        self.theta=ANGLE
        self.vl=5
        self.vr=5
        self.control_signal = 0
        self.x_front = self.x + 100 * math.cos(self.theta)
        self.y_front = self.y + 100 * math.sin(self.theta)


    def rotate_point(c, angle:float, point)->tuple: #c center
        """rotating a point around another point
        which is not at the origin
        """
        pointx,pointy=point
        cx,cy=c
        s=math.sin(angle)
        c=math.cos(angle)
        
        #translation towards the origin:
        pointx=pointx-cx
        pointy=pointy-cy
        #preform rotation
        xnew=pointx*c - pointy * s
        ynew=pointx*s + pointy * c
        #translation back
        pointx=xnew+cx
        pointy = ynew + cy
        return pointx,pointy

    def dist(self,a,b):
        result = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        return result

    def move(self,dt):
        self.x += ((self.vl+self.vr)/2)*math.cos(self.theta)*dt
        self.y -= ((self.vl+self.vr)/2)*math.sin(self.theta)*dt
        self.theta += (self.move_angle)/10 * dt

        self.x_front = self.x + 50 * math.cos(self.theta)
        self.y_front = self.y + 50 * math.sin(self.theta)

    def new_move(self,dt):
        target = self.targets[self.waypoint]    #w= vitesse angulaire    u= vitesse lineaire
        delta_x = target[0] - self.x
        delta_y = target[1] - self.y 
        self.u = 10 #delta_x * math.cos(self.theta) + delta_y * math.sin(self.theta)
        #self.w = (-1/30) * math.sin(self.theta) * delta_x + (1/30) * math.cos(self.theta) * delta_y
        self.w = self.control_signal
        
        self.x += (self.u*math.cos(self.theta) - 30*math.sin(self.theta)*self.w)*dt
        self.y += (self.u*math.sin(self.theta) + 30*math.cos(self.theta)*self.w)*dt
        self.theta += self.w*dt

        self.x_front = self.x + 50 * math.cos(self.theta)
        self.y_front = self.y + 50 * math.sin(self.theta)

        if self.dist((self.x,self.y),target) <=10:
            self.waypoint +=1

        if self.waypoint >= len(self.targets)-1:
            self.waypoint = len(self.targets)-1
            self.u = 0


    def controller(self,input:float,setpoint:float)->None:
        pid = PID(0.1, 0, 0.1, setpoint)
        control_sig = pid(input)
        self.control_signal = control_sig
        print('pid output :',self.control_signal)
        print('angle: ',input)


_, path = rrt_planning()
our_map = pygame.image.load('ourMap.jpeg')
running = True
dt = 0.001
prev_time = time.time()
R = Robot(p2,angle,list(reversed(path)))
ENV = Envir((720,1280))

while running:
    ENV.map.blit(our_map,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
    
    angle = desired_angle((np.array((R.x_front,R.y_front)),np.array((R.x,R.y)),R.targets[R.waypoint]))
    R.controller(input=angle, setpoint=180)
    R.new_move(dt)
    ENV.draw_robot((R.x,R.y),(R.x_front,R.y_front))
    ENV.draw_path(path)
    pygame.display.flip()
    #ENV.map.fill(ENV.white)
    dt = time.time() - prev_time
    prev_time = time.time()





 