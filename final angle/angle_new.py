from distutils.util import execute
import numpy as np
from numpy import pi
import pygame
import sched, time
import math

s = sched.scheduler(time.time, time.sleep)
t1=0
t1=time.time()
 

background_colour = (255,255,255) # For the background color of your window
(width, height) = (800, 700) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('the man with the if') # Name for the window
screen.fill(background_colour) #This syntax fills the background colour



p1 = np.array([300,300])
p2 = np.array([400,400])
p3 = np.array([500,300])

point1= pygame.draw.circle(screen, (255, 0, 0), p1, 7, 0) #R
point2= pygame.draw.circle(screen, (0, 255, 0), p2, 7, 0) #G
Point3= pygame.draw.circle(screen, (0, 0, 255), p3, 7, 0) #B

pygame.display.flip()

U = p1 - p2
V = p3 - p2

cosine_angle = np.dot(U, V) / (np.linalg.norm(U) * np.linalg.norm(V))
angle = np.arccos(cosine_angle)



# adjust for hemisphere
if V[0] < 0: angle=360 - np.degrees(angle)
if V[0] > 0: angle=np.degrees(angle)



while True:
    print (angle)
    
    if angle == 180:
        
        print ('move forward')
        time.sleep(2)
    elif angle < 180:
        print ('translate left')
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
