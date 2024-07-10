import pygame
import sys

class movementBus:
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana");
    numberOfYellowStripImg=7
    mouse=pygame.mouse.get_pos()
    cont=0
    stopCont=0
    stationStop=0
    acceleration=1
    numberImg=1
    personCont=0
    movPerson=1
    pauseMov=0
def fund():
     font=pygame.font.SysFont(None,20) 
     x=(800*0.45)
     y=(600*0.8)
     #floortextureImg= pygame.image.load("grass.jpeg")
     #stripImg= pygame.image.load("strip.jpg")
     #yellowStripImg=pygame.image.load("yellow_strip.jpg")
   
     #main.screen.blit(floortextureImg,(-150,0));
     #main.screen.blit(floortextureImg,(700,0));
     #main.screen.blit(yellowStripImg, (400,0))
     #main.screen.blit(yellowStripImg, (400,100))
     #main.screen.blit(yellowStripImg, (400,200))
     #main.screen.blit(yellowStripImg, (400,300))
     #main.screen.blit(yellowStripImg, (400,400))
     #main.screen.blit(yellowStripImg, (400,500))
     #main.screen.blit(yellowStripImg, (400,600))
     #main.screen.blit(stripImg, (130,0))
     #main.screen.blit(stripImg, (670,0))
     
      
     moneyCollected=font.render("Money collected", True, (255,255,255))
     maximumCapacity=font.render("Maximum capacity", True, (0,0,0))
     passengers=font.render("Passengers", True, (0,0,0))
     movementBus.screen.blit(moneyCollected, (460,25))
     movementBus.screen.blit(maximumCapacity, (460,75))
     movementBus.screen.blit(passengers, (460,125)) 
def movementStrip():
     floortextureImg= pygame.image.load("grass.png")
     stripImg= pygame.image.load("strip.jpg")
     yellowStripImg=pygame.image.load("yellow_strip.jpg")
     stopImg=pygame.image.load("stop.png")
     person=pygame.image.load("persprue.png")
   
     if movementBus.numberImg<=10:
      recreoStopImg=pygame.image.load("shutdown"+repr(movementBus.numberImg)+".png")
      rel_y = movementBus.numberOfYellowStripImg % 103
      movementBus.screen.blit(floortextureImg, (0, rel_y - 103))
      movementBus.screen.blit(floortextureImg, (700, rel_y - 103))
      movementBus.cont+=1
  
     if rel_y < 800:
       movementBus.screen.blit(floortextureImg, (0, rel_y))
       movementBus.screen.blit(floortextureImg, (700, rel_y))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y + 100))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y + 200))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y + 300))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y + 400))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y + 500))
       movementBus.screen.blit(yellowStripImg,  (400, rel_y - 100))
       movementBus.screen.blit(stripImg, (130, rel_y - 300))
       movementBus.screen.blit(stripImg, (130, rel_y + 20))
       movementBus.screen.blit(stripImg, (130, rel_y + 30))
       movementBus.screen.blit(stripImg, (670, rel_y - 300))
       movementBus.screen.blit(stripImg, (670, rel_y + 20))
       movementBus.screen.blit(stripImg, (670, rel_y + 30))
       if movementBus.cont>1000 and (movementBus.stopCont%800-200)<580:
           movementBus.stopCont+=movementBus.acceleration
           movementBus.screen.blit(stopImg, (0, movementBus.stopCont%800-200))    
           
       if (movementBus.stopCont%800-200)>-80 and (movementBus.stationStop%800-200)<580:
              movementBus.stationStop+=movementBus.acceleration
              movementBus.screen.blit(recreoStopImg,(0,movementBus.stationStop%800-200))
             
       if movementBus.acceleration>0:       
        if(movementBus.stationStop%800-200)>0 and (movementBus.personCont%800-200)<45:
          movementBus.personCont+=movementBus.acceleration
          movementBus.screen.blit(person,(60 ,movementBus.personCont-10))  
          movementBus.pauseMov=0
        

       else:
          if movementBus.pauseMov<40:
           movementBus.personCont+=movementBus.movPerson
           movementBus.screen.blit(person,(movementBus.personCont%150,236)) 
           movementBus.pauseMov+=1
          
       movementBus.numberOfYellowStripImg += movementBus.acceleration
       if movementBus.cont<=583:
         if movementBus.cont%53==0 and movementBus.acceleration<20:      
          if movementBus.acceleration<=11:
            movementBus.acceleration+=1 
            
         
       else:
         if movementBus.cont%53==0 and movementBus.cont<=1219 :
          movementBus.acceleration+=-1  
          
       if movementBus.cont>1400 and movementBus.cont>2200:
          if movementBus.cont%53==0 and movementBus.acceleration<20:      
           if movementBus.acceleration<=11:
            movementBus.acceleration+=1 
           
       if movementBus.cont==2400 :
        movementBus.stopCont=0
        movementBus.personCont=0
        movementBus.stationStop=0
        movementBus.numberImg+=1
        movementBus.cont=0
def busPositioning(x,y):
     busImg=pygame.image.load("staffBus.png")
     busInsideImg=pygame.image.load("busInside.png")
     movementBus.screen.blit(busImg,(700,200))  
     movementBus.screen.blit(busInsideImg,(100,50)) 
def framework():
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        movementBus.screen.fill((119, 119, 119))
        movementBus.mouse = pygame.mouse.get_pos()  
         
        fund();
        movementStrip();
        busPositioning(0,0)   
        pygame.display.flip()
 
        

pass




