from numpy import arccos
from numpy import pi

import pygame
import math

background_colour = (255,255,255) # For the background color of your window
(width, height) = (800, 700) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('the man with the if') # Name for the window
screen.fill(background_colour) #This syntax fills the background colour
#___________

x1= 100
y1=300
x2= 300
y2= 100
x3= 500
y3= 200
point1= pygame.draw.circle(screen, (255, 0, 0), [x1, y1], 7, 0) #R
point2= pygame.draw.circle(screen, (0, 255, 0), [x2, y2], 7, 0) #G
Point3= pygame.draw.circle(screen, (0, 0, 255), [x3, y3], 7, 0) #B
pygame.display.flip()
#___________
#def angle():
U= [(x2-x1),(y2-y1)]
V= [(x3-x2),(y3-y2)]
products = U[0]*V[0]+U[1]*V[1]
print ("products =", products)
modulous1 = math.sqrt((U[0]**2)+(U[1]**2))
modulous2 = math.sqrt((V[0]**2)+(V[1]**2))
modulous = modulous1*modulous2
print ('m= ', modulous)
cos= products/modulous
angle = arccos(cos)*360/(2*pi)
print ('angle', angle)
'''
if y1 == y2:
    if angle > 0 :
        print ('rotate right and move forward')
    if angle < 0 :
        print ('rotate left and move forward')
else
'''


#___________
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()