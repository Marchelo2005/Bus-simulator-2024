import pygame
from utils.constants.constantWindow.constantWindow import window
from movementBus.imgEnvironment.img import environment
from utils.variables.variable.variable import variable

class grass():
  def movementGrass():
    window.rel_y= window.numberOfYellowStripImg % 103
    window.screen.blit(environment.floortextureImg, (0, window.rel_y - 103))
    window.screen.blit(environment.floortextureImg, (700, window.rel_y - 103))
    variable.cont+=1 
  def movementGrassXY():
    window.rel_y= window.numberOfYellowStripImg % 103
    window.screen.blit(environment.floortextureImg, (0, window.rel_y))
    window.screen.blit(environment.floortextureImg, (700, window.rel_y))
    
    