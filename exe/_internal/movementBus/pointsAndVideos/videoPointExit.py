import pygame; import random
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window
from utils.faceDetector.face_detector import detector
from movementBus.pointsAndVideos.drawPoint.deletePoint import deletePoint

def videoPointExit():
 probabilityOfPeopleDrop=random.randint(0,2)
 variable.positionOfOutputMovement-=1
 if variable.positionOfOutputMovement==100 and variable.numberImg>1 and (probabilityOfPeopleDrop==0 or probabilityOfPeopleDrop==1):
  randomSeat = random.randint(2,12) 
  if len(variable.drawnPoints )-randomSeat<0:
   randomSeat=3  
  for numberRandomVideo in range (1,randomSeat,1):
   detector.txtVideo="exit"
   detector.face()
   pygame.display.set_mode(window.size)
   pygame.display.set_caption("window")
   variable.orderMovement=True
   deletePoint()
   
