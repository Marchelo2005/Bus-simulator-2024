import random
from utils.variables.variable.variable import variable

def deletePoint():
  randomSeat = random.randint(0, len(variable.drawnPoints)-1)  
  del (variable.drawnPoints[randomSeat])
  
