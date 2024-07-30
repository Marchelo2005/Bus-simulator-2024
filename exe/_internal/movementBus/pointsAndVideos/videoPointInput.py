import pygame
import random; from utils.constants.constantPoint.constantPoint import coordinate
from utils.variables.variable.variable import variable; from utils.constants.constantWindow.constantWindow import window
from utils.faceDetector.face_detector import detector; from movementBus.pointsAndVideos.drawPoint.drawPoint import drawPoint

def videoPointInput():
 randomSeat = random.randint(2,24) 
 if len(variable.drawnPoints)+randomSeat>31:
   randomSeat=(30-len(variable.drawnPoints)+1)
 for numberRandomVideo in range (1, randomSeat, 1):
   detector.txtVideo="person"
   detector.face()
   drawPoint(coordinate.points)
   variable.totalMoneyRaised += 0.35 
   pygame.display.set_mode(window.size)
   pygame.display.set_caption("window")
   variable.busySeat=True
   variable.orderMovement=False
 variable.positionOfOutputMovement=135 