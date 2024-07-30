from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window

class movement():
 def resetMovement():
  if variable.cont==2200 :
   variable.stopCont=0
   variable.personCont=0
   variable.stationStop=0
   variable.numberImg+=1
   variable.cont=0
 def restart():
  variable.passengerCounter=0
  variable.totalMoneyRaised=0
  window.rel_y=0
  variable.drawnPoints.clear()
  variable.cont, variable.stopCont, variable.stationStop, variable.personCont, variable.pauseMov = 0, 0, 0, 0, 0
  variable.acceleration,variable.numberImg, variable.movPerson=1,1,1
    
