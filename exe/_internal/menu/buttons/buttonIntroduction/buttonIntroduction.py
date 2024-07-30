import pygame
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons
from menu.mainMenu.instruction.instruction import instruction

def introduction(mouse,click):
 if 336 < mouse[0] < 485 and 280 < mouse[1] < 330:
  pygame.draw.rect(window.screen, color.silver, (327, 280, 165, 50))
  if click == (1, 0, 0):
   instruction()
 else:
  pygame.draw.rect(window.screen, color.white, (327, 280, 165, 50))
 
 Buttons.createButton(window.screen,327, 280, 165, 50,"INTRODUCTION")
