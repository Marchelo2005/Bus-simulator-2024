import pygame
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons

def back(click):
 pygame.draw.rect(window.screen, color.silver, (650, 5, 150, 50))  
 if click == (1, 0, 0):
   from menu.mainMenu.introLoop.introLoop import introLoop
   introLoop()    
 else:
  pygame.draw.rect(window.screen, color.white, (650, 5, 150, 50)) 
 Buttons.createButton(window.screen,650, 5, 150, 50,"BACK")

