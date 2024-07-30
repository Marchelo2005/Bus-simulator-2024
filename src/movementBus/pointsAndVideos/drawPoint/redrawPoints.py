import pygame
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color

def redrawPoints():
  for point in variable.drawnPoints:
   pygame.draw.circle(window.screen, color.red, point, 5)   