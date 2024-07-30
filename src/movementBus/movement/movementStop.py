import pygame
from movementBus.imgEnvironment.img import environment
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window

def stop():
 if variable.cont>1000 and (variable.stopCont%800-200)<580:
  variable.stopCont+=variable.acceleration
  window.screen.blit(environment.stopImg, (0, variable.stopCont%800-200))  
