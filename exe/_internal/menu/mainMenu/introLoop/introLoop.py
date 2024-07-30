import pygame; import sys
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttonStart.buttonStart import Start
from menu.buttons.buttons import Buttons
from menu.buttons.buttonIntroduction.buttonIntroduction import introduction
from menu.buttons.buttonClose.buttonClose import Close

def introLoop():
     window()
     pygame.init()
     introImage = pygame.image.load("assets/assetsInterface/PORTADA1.png")
     while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
        window.screen.blit(introImage, (0, 0))
        Buttons.buttonDrawing(window.screen, color.white, 80, 280, 150, 50)
        Buttons.buttonDrawing(window.screen, color.white, 327, 280, 165, 50)
        Buttons.buttonDrawing(window.screen, color.white, 580, 280, 150, 50)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        Start(mouse,click)
        introduction(mouse,click)
        Close(mouse,click)
        pygame.display.flip()
        
        
        