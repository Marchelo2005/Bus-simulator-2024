
from cgitb import small
from dis import Instruction
from turtle import Screen, back, title
from webbrowser import BackgroundBrowser
import pygame
import sys





#colors
white =(255,255,255)
silver=(192,192,192)
##color punto##
red = (255, 0, 0)

class main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana");
    numberOfYellowStripImg=7
    
    #se agrego la interzas
    intro_image = pygame.image.load("PORTADA1.png")
    instruction_background=pygame.image.load("intruction1.png")
 ##agregar punto##
    points = [(175,230),(196,230),(175,294),(197,294),(172,324),
              (195,324),(174,357), (195,354), 
              (172,388),(196,388),(172,461),(196,461),
              (172,496),(197,496),(221,496),(245,496),
              (267,496),(266,422),
              (244,422),(265,393),(243,393),(266,393),
              (244,360),(266,358),(243,357),(267,325),
              (243,327),(265,325),(266,294),
              (243,294),(266,263),(243,263),(266,228)]
   
def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        main.screen.blit(main.intro_image,(0,0))  
        
   
        
       
        pygame.draw.rect(main.screen,white,(80,280,150,50))
        pygame.draw.rect(main.screen,white,(327,280,165,50))
        pygame.draw.rect(main.screen,white,(580,280,150,50))
         ##funtion the botons ##
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        #print(click)
        

        print(mouse)
        
        if mouse[0] >80 and mouse[0]<230 and mouse[1]>280 and mouse[1]<330:
            pygame.draw.rect(main.screen,silver,(80,280,150,50))
            if click ==(1,0,0):
                framework()
        else:
           pygame.draw.rect(main.screen,white,(80,280,150,50)) 
        
        smallText =pygame.font.Font("freesansbold.ttf",20)
        textSurface,textRect=text_objects("START",smallText)
        textRect.center =((80+(150/2)),(280+(50/2)))
        main.screen.blit(textSurface,textRect)

        if mouse[0] >336 and mouse[0]<485 and mouse[1]>280 and mouse[1]<330:
            pygame.draw.rect(main.screen,silver,(327,280,165,50))
            if click==(1,0,0):
                instruction()
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(main.screen,white,(327,280,165,50))
           
        smallText =pygame.font.Font("freesansbold.ttf",20)
        textSurface,textRect=text_objects("INTRODUCTION",smallText)
        textRect.center =((336+(150/2)),(280+(50/2)))
        main.screen.blit(textSurface,textRect)
        
        if mouse[0] >580 and mouse[0]<730 and mouse[1]>280 and mouse[1]<330:
            pygame.draw.rect(main.screen,silver,(580,280,150,50))
            if click==(1,0,0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(main.screen,white,(580,280,150,50))

        smallText =pygame.font.Font("freesansbold.ttf",20)
        textSurface,textRect=text_objects("CLOSE",smallText)
        textRect.center =((580+(150/2)),(280+(50/2)))
        main.screen.blit(textSurface,textRect)

        pygame.display.update()
        

        #

def instruction():
    instruction=True
    clock = pygame.time.Clock()
    while instruction:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
         

        main.screen.blit(main.instruction_background,(0,0))
        
        largetext =pygame.font.Font("freesansbold.ttf",80)
        mediumtext =pygame.font.Font("freesansbold.ttf",40)
        smalltext =pygame.font.Font("freesansbold.ttf",20)
        
        pygame.draw.rect(main.screen,white,(650,5,150,50))
        
        
        mouse =pygame.mouse.get_pos()
        if mouse[0]>580 and mouse[0]<730 and mouse[1]>300 and mouse[1]<350:
            pygame.draw.rect(main.screen,silver,(650,5,150,50))
        else:
            pygame.draw.rect(main.screen,white,(650,5,150,50))
            
            smallText=pygame.font.Font("freesansbold.ttf",20)
        textSurface,textRect =text_objects("BACK",smallText)
        textRect.center =(650+(150/2),5+(50/2))
        main.screen.blit(textSurface,textRect)
        
        click =pygame.mouse.get_pressed()
        if click == (1,0,0):
            intro_loop()
        

            
        pygame.display.update()
        clock.tick(30)

def text_objects(text,font):
    textSurface=font.render(text,True,(0,0,0))
    return textSurface,textSurface.get_rect()


def timeMovement():
    clock= pygame.time.Clock()
    clock.tick(100)
def fund():
    font=pygame.font.SysFont(None,20) 
    x=(800*0.45)
    y=(600*0.8)
    floortextureImg= pygame.image.load("grass.jpeg")
    stripImg= pygame.image.load("strip.jpg")
    yellowStripImg=pygame.image.load("yellow_strip.jpg")
   
    main.screen.blit(floortextureImg,(-150,0));
    main.screen.blit(floortextureImg,(700,0));
    main.screen.blit(yellowStripImg, (400,0))
    main.screen.blit(yellowStripImg, (400,100))
    main.screen.blit(yellowStripImg, (400,200))
    main.screen.blit(yellowStripImg, (400,300))
    main.screen.blit(yellowStripImg, (400,400))
    main.screen.blit(yellowStripImg, (400,500))
    main.screen.blit(yellowStripImg, (400,600))
    main.screen.blit(stripImg, (130,0))
    main.screen.blit(stripImg, (670,0))
     
      
    moneyCollected=font.render("Money collected", True, (255,255,255))
    maximumCapacity=font.render("Maximum capacity", True, (0,0,0))
    passengers=font.render("Passengers", True, (0,0,0))
    main.screen.blit(moneyCollected, (460,25))
    main.screen.blit(maximumCapacity, (460,75))
    main.screen.blit(passengers, (460,125)) 
 
"""def movementStrip():
    floortextureImg= pygame.image.load("grass.jpeg")
    stripImg= pygame.image.load("strip.jpg")
    yellowStripImg=pygame.image.load("yellow_strip.jpg")
    rel_y = main.numberOfYellowStripImg % floortextureImg.get_rect().width
    main.screen.blit(yellowStripImg, (-150, rel_y - floortextureImg.get_rect().width))
    main.screen.blit(yellowStripImg, (700, rel_y - floortextureImg.get_rect().width))
    if rel_y < 800:
       main.screen.blit(floortextureImg, (-150, rel_y))
       main.screen.blit(floortextureImg, (700, rel_y))
       main.screen.blit(yellowStripImg,  (400, rel_y))
       main.screen.blit(yellowStripImg,  (400, rel_y + 100))
       main.screen.blit(yellowStripImg,  (400, rel_y + 200))
       main.screen.blit(yellowStripImg,  (400, rel_y + 300))
       main.screen.blit(yellowStripImg,  (400, rel_y + 400))
       main.screen.blit(yellowStripImg,  (400, rel_y + 500))
       main.screen.blit(yellowStripImg,  (400, rel_y - 100))
       main.screen.blit(stripImg, (130, rel_y - 200))
       main.screen.blit(stripImg, (130, rel_y + 20))
       main.screen.blit(stripImg, (130, rel_y + 30))
       main.screen.blit(stripImg, (670, rel_y - 100))
       main.screen.blit(stripImg, (670, rel_y + 20))
       main.screen.blit(stripImg, (670, rel_y + 30))
       main.numberOfYellowStripImg += 7 """

def busPositioning(x,y):
    busImg=pygame.image.load("staffBus.png")
    busInsideImg=pygame.image.load("busInside.png")
    main.screen.blit(busImg,(700,200))  
    main.screen.blit(busInsideImg,(100,50)) 
    
 ##dibujar los puntos##
def draw_points(points):
    for point in points:
        pygame.draw.circle(main.screen, red, point, 5)



def framework():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        main.screen.fill((119, 119, 119))
        fund();
##agregar punto
def framework():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        main.screen.fill((119, 119, 119))
        fund()
        
        busPositioning(0, 0)
        
        # Llamada para dibujar el punto rojo
        draw_points(main.points)  # Coordenadas del punto rojo

        pygame.display.flip()

        intro_loop()
#################################
        movementStrip();
        busPositioning(0,0)   
        pygame.display.flip()
        

        intro_loop();  

framework();
