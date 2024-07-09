import pygame
import sys

class main(object):
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
     main.screen.blit(moneyCollected, (460,25))
     main.screen.blit(maximumCapacity, (460,75))
     main.screen.blit(passengers, (460,125)) 
    def movementStrip():
     floortextureImg= pygame.image.load("grass.png")
     stripImg= pygame.image.load("strip.jpg")
     yellowStripImg=pygame.image.load("yellow_strip.jpg")
     stopImg=pygame.image.load("stop.png")
     person=pygame.image.load("persprue.png")
   
     if main.numberImg<=10:
      recreoStopImg=pygame.image.load("shutdown"+repr(main.numberImg)+".png")
      rel_y = main.numberOfYellowStripImg % 103
      main.screen.blit(floortextureImg, (0, rel_y - 103))
      main.screen.blit(floortextureImg, (700, rel_y - 103))
      main.cont+=1
  
     if rel_y < 800:
       main.screen.blit(floortextureImg, (0, rel_y))
       main.screen.blit(floortextureImg, (700, rel_y))
       main.screen.blit(yellowStripImg,  (400, rel_y))
       main.screen.blit(yellowStripImg,  (400, rel_y + 100))
       main.screen.blit(yellowStripImg,  (400, rel_y + 200))
       main.screen.blit(yellowStripImg,  (400, rel_y + 300))
       main.screen.blit(yellowStripImg,  (400, rel_y + 400))
       main.screen.blit(yellowStripImg,  (400, rel_y + 500))
       main.screen.blit(yellowStripImg,  (400, rel_y - 100))
       main.screen.blit(stripImg, (130, rel_y - 300))
       main.screen.blit(stripImg, (130, rel_y + 20))
       main.screen.blit(stripImg, (130, rel_y + 30))
       main.screen.blit(stripImg, (670, rel_y - 300))
       main.screen.blit(stripImg, (670, rel_y + 20))
       main.screen.blit(stripImg, (670, rel_y + 30))
       if main.cont>1000 and (main.stopCont%800-200)<580:
           main.stopCont+=main.acceleration
           main.screen.blit(stopImg, (0, main.stopCont%800-200))    
           
       if (main.stopCont%800-200)>-80 and (main.stationStop%800-200)<580:
              main.stationStop+=main.acceleration
              main.screen.blit(recreoStopImg,(0,main.stationStop%800-200))
             
       if main.acceleration>0:       
        if(main.stationStop%800-200)>0 and (main.personCont%800-200)<45:
          main.personCont+=main.acceleration
          main.screen.blit(person,(60 ,main.personCont-10))  
          main.pauseMov=0
        

       else:
          if main.pauseMov<40:
           main.personCont+=main.movPerson
           main.screen.blit(person,(main.personCont%150,236)) 
           main.pauseMov+=1
          
       main.numberOfYellowStripImg += main.acceleration
       if main.cont<=583:
         if main.cont%53==0 and main.acceleration<20:      
          if main.acceleration<=11:
            main.acceleration+=1 
            
         
       else:
         if main.cont%53==0 and main.cont<=1219 :
          main.acceleration+=-1  
          
       if main.cont>1400 and main.cont>2200:
          if main.cont%53==0 and main.acceleration<20:      
           if main.acceleration<=11:
            main.acceleration+=1 
           
       if main.cont==2400 :
        main.stopCont=0
        main.personCont=0
        main.stationStop=0
        main.numberImg+=1
        main.cont=0

    def busPositioning(x,y):
     busImg=pygame.image.load("staffBus.png")
     busInsideImg=pygame.image.load("busInside.png")
     main.screen.blit(busImg,(700,200))  
     main.screen.blit(busInsideImg,(100,50)) 
    def framework():
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        main.screen.fill((119, 119, 119))
        main.mouse = pygame.mouse.get_pos()  
         
        fund();
        movementStrip();
        busPositioning(0,0)   
        pygame.display.flip()
 
    framework();
    pass




