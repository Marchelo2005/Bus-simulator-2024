
import pygame
import sys

class main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana");

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
    main.screen.blit(moneyCollected, (0,50))
    main.screen.blit(maximumCapacity, (0,100))
    main.screen.blit(passengers, (0,150))
                           
def busPositioning(x,y):
    busImg=pygame.image.load("staffBus.png")
    busInsideImg=pygame.image.load("busInside.png")
    radar=pygame.image.load("radar.gif")
    main.screen.blit(radar, (700,200))
    main.screen.blit(busImg,(700,200)) 
    main.screen.blit(busInsideImg,(200,50)) 
    
    
def framework():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()        
        main.screen.fill((119, 119, 119))
        fund();
        busPositioning(0,0)   
        pygame.display.flip()
        
framework();