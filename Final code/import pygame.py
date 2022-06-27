import pygame
import math

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
        pygame.display.set_caption("Diffenretial drive robot")
        self.map=pygame.display.set_mode((self.width,self.height))
        #text variables
        
        self.font=pygame.font.Font('freesansbold.ttf',50)
        self.text=self.font.render('defalt',True,self.white,self.black)
        self.textRect=self.text.get_rect()
        self.textRect.center=(dimention[1]-600,dimention[0]-100)

        

    def write_info(self,Vl,Vr,theta):
        txt=f"Vl = {Vl} Vr = {Vr} theta = {int(math.degrees(theta))}"
        self.text=self.font.render(txt,True,self.white,self.black)
        self.map.blit(self.text,self.textRect)



class Robot:

    def __init__(self,startpos,robotImg,width):
        self.m2p=3779.52

        self.w=width
        self.x=startpos[0]
        self.y=startpos[1]
        self.theta=0 
        self.vl=0.01*self.m2p
        self.vr=0.01*self.m2p
        #graphics
        self.maxspeed=0.02*self.m2p
        self.minspeed=0.02*self.m2p 
        #graphic
        self.img=pygame.image.load(robotImg)
        self.rotated=self.img
        self.rect=self.rotated.get_rect(center=(self.x,self.y))


    def draw(self,map):
        map.blit(self.rotated,self.rect) 
    
    def move(self, event=None):
        
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP4:
                    self.vl+=0.001*self.m2p
                elif event.key == pygame.K_KP1:
                   self.vl-=0.001*self.m2p
                elif event.key == pygame.K_KP6:
                   self.vr+=0.001*self.m2p
                elif event.key == pygame.K_KP3:
                   self.vr-=0.001*self.m2p
            
                              

        self.x+=((self.vl+self.vr)/2)*math.cos(self.theta)*dt
        self.y-=((self.vl+self.vr)/2)*math.sin(self.theta)*dt
        self.theta+=(self.vr-self.vl)/self.w*dt

        self.rotated=pygame.transform.rotozoom(self.img,math.degrees(self.theta),1)
        self.rect=self.rotated.get_rect(center=(self.x,self.y))
        

#initialisation
pygame.init()

#start position
start=(200,200)

#dimention
dims=(600,1200)

#running or not 
running=True

#the envir
environment=Envir(dims) 

#the robot
robot=Robot(start,r"C:\Users\acer\CARimage.png",0.01*3779.52) 
dt=0
lasttime=pygame.time.get_ticks()
#simulation loop
while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running=False
       robot.move(event)
        
    dt=(pygame.time.get_ticks()-lasttime)/1000
    lasttime=pygame.time.get_ticks()
    pygame.display.update()
    environment.map.fill(environment.black)  
    robot.move()  
    robot.draw(environment.map) 
    environment.write_info(int(robot.vl),int(robot.vr),robot.theta)    
