import pygame
from movementBus.movement.movementGrass import grass; from utils.variables.variable.variable import variable; from utils.constants.constantWindow.constantWindow import window; from movementBus.movement.movementShutdown import movementShutdown; from utils.constants.constantPoint.constantPoint import coordinate
from movementBus.movement.movementPerson import movementPerson; from movementBus.speed.speed import acceleration; from utils.dataBase.InsertTable.insertTable import insertRecord
from movementBus.movement.movementStrip import movementStrip; from movementBus.movement.movementStop import stop; from movementBus.pointsAndVideos.videoPointInput import videoPointInput; from movementBus.pointsAndVideos.videoPointExit import videoPointExit
from movementBus.valueReset.valueReset import movement; from movementBus.imgEnvironment.img import environment; from movementBus.valueReset.valueReset import movement

def movementBus():
  from menu.mainMenu.introLoop.introLoop import introLoop
  environment()
  if variable.numberImg==11:
    insertRecord(variable.totalMoneyRaised)
    movement.restart()
    introLoop()
  else:
    grass.movementGrass()
    shutDown=pygame.image.load("assets/assetsShutdown/shutdown"+repr(variable.numberImg)+".png")  
  grass.movementGrassXY()
  movementStrip()
  stop()
  movementShutdown(shutDown)
  if variable.acceleration>0 and len(variable.drawnPoints)!=len(coordinate.points): 
   movementPerson.movementPersonEnvironment()
  else:
   if variable.pauseMov < 40 and len(variable.drawnPoints)!=len(coordinate.points) : 
    movementPerson.movementPersonBusInput()
    if variable.pauseMov==40: 
     videoPointInput()
     variable.pauseMov += 1
   else:
    videoPointExit()
   movementPerson.movementPersonBusExit()
  window.numberOfYellowStripImg += variable.acceleration
  acceleration.accelerationAndDeceleration()
  acceleration.nullAcceleration()
  movement.resetMovement()
  
   