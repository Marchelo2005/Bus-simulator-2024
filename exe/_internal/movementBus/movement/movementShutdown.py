import pygame
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window

def movementShutdown(shutdown):
 if (variable.stopCont%800-200)>-80 and (variable.stationStop%800-200)<580:
   variable.stationStop+=variable.acceleration
   window.screen.blit(shutdown,(0,variable.stationStop%800-200))
