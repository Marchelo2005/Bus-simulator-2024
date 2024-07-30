import pygame
import random
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color

def drawPoint(points): 
  randomSeat = random.randint(0, len(points) - 1)
  point = points[randomSeat]
  if point not in variable.drawnPoints:
    variable.drawnPoints.append(point)
    pygame.draw.circle(window.screen, color.red, point, 5)
    variable.busySeat = False
  else:
    variable.busySeat = True
    while variable.busySeat:
     randomSeat = random.randint(0, len(points) - 1)
     point = points[randomSeat]
     if point not in variable.drawnPoints:
       variable.drawnPoints.append(point)
       pygame.draw.circle(window.screen, color.red, point, 5)
       variable.busySeat = False
