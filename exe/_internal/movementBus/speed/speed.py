from utils.variables.variable.variable import variable

class acceleration():
 
 def accelerationAndDeceleration(): 
  if variable.cont<=583:
   if variable.cont%53==0 and variable.acceleration<=11:
    variable.acceleration+=1 
  elif variable.cont%53==0 and variable.cont<=1219 :
   variable.acceleration+=-1  
   
 def nullAcceleration():
  if variable.cont>2000:
   if variable.cont%53==0 and variable.acceleration<=11:
    variable.acceleration+=1
