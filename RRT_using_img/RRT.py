import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time

def main():
    map_path = 'C:\\Users\\amine\\Desktop\\codings\\Final\\img\\simu2.jpg'
    start=(50,50)
    goal=(700,600)
    iteration=0
    t1=0

    pygame.init()
    map=RRTMap(start,goal,map_path)
    graph=RRTGraph(start,goal,(map.mapw,map.maph))

    map.drawMap()

    t1=time.time()
    
    while (not graph.path_to_goal()):
        print('time',t1)
        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        #raise exception if timeout
        if elapsed > 10:
            print('timeout re-initiating the calculations')
            raise

        if iteration % 10 == 0:
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
    pygame.event.clear()
    pygame.event.wait(0)
    


if __name__ == '__main__':
    main()




























