import pygame
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons
from menu.buttons.buttonBack.buttonBack import back
import sys

def instruction():
   window()
   instructionBackground = pygame.image.load("assets/assetsInterface/intruction1.png")
   while True:
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
             sys.exit()
     click = pygame.mouse.get_pressed()
     window.screen.blit(instructionBackground, (0, 0))
     Buttons.buttonDrawing(window.screen, color.white, 650, 5, 150, 50)
     back(click)
     pygame.display.flip() 
     