import pygame
from utils.variables.variable.variable import variable
from movementBus.imgEnvironment.img import environment
from utils.constants.constantWindow.constantWindow import window

class movementPerson():
  def movementPersonEnvironment():
   if(variable.stationStop%800-200)>0 and (variable.personCont%800-200)<45:
     variable.personCont+=variable.acceleration
     window.screen.blit(environment.person,(60 ,variable.personCont-10))  
     variable.pauseMov=0    

  def movementPersonBusInput():
     variable.personCont += variable.movPerson
     window.screen.blit(environment.person, (variable.personCont % 150, 236))
     variable.pauseMov += 1
  def movementPersonBusExit():
     if variable.positionOfOutputMovement>0 and variable.positionOfOutputMovement<50 and variable.orderMovement==True:
      window.screen.blit(environment.person, (variable.positionOfOutputMovement%135,416))