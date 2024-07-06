
from turtle import back
from webbrowser import BackgroundBrowser
import pygame
import sys

class main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana");
    numberOfYellowStripImg=7

def timeMovement():
    clock= pygame.time.Clock()
    clock.tick(100)
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
       main.numberOfYellowStripImg += 7

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
        fund();
        movementStrip();
        busPositioning(0,0)   
        pygame.display.flip()
        
framework();