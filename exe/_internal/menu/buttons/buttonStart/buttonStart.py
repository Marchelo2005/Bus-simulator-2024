import pygame
from framework.framework import framework

from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons

def Start(mouse,click):
 if 80 < mouse[0] < 230 and 280 < mouse[1] < 330:
  pygame.draw.rect(window.screen, color.silver, (80, 280, 150, 50))
  if click[0] == 1:
   framework()
 else:
  pygame.draw.rect(window.screen, color.white, (80, 280, 150, 50))
 
 Buttons.createButton(window.screen,80,280,150,50,"START")