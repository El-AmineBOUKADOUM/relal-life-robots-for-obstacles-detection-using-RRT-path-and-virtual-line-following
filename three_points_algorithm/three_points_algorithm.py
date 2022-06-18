import pygame

background_colour = (255,255,255) # For the background color of your window
(width, height) = (800, 700) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('the man with the if') # Name for the window
screen.fill(background_colour) #This syntax fills the background colour
#___________

x1= 400
y1=200
x2= 200
y2= 250
x3= 300
y3= 400
point1= pygame.draw.circle(screen, (255, 0, 0), [y1, x1], 7, 0)
point2= pygame.draw.circle(screen, (0, 255, 0), [y2, x2], 7, 0)
Point3= pygame.draw.circle(screen, (0, 0, 255), [y3, x3], 7, 0)
pygame.display.flip()

if x1 == x2:
    if x3 == x2:
        print ('good, move forward')
    else:
        print ('x3 != x2')
        while x2 > x3:
            print ('turn left')
        while x2 < x3:
            print ('turn right')
elif y1 == y2:     
    if y3 == y2:
        print ('good, move forward')
    else:
        print ('y3 != y2')
        while y2 > y3:
            print ('go up')
        while y2 < y3:
            print ('go down')
elif x1 != x2 & y1 != y2:
    if x3 == x2:
        print ('good, move forward')
    elif x3 != x2:
        print ('x3 != x2')
        while x2 > x3:
            print ('turn left')
        while x2 < x3:
            print ('turn right')
    if y3 == y2:
        print ('good, move forward')
    elif y3 != y2:
        print ('y3 != y2')
        while y2 > y3:
            print ('go up')
        while y2 < y3:
            print ('go down')

#___________



running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()