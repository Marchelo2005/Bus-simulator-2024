import pygame
from utils.constants.constantWindow.constantWindow import window; from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons
from movementBus.movement.movementStrip import movementStrip

def continueButton(mouse,click):
  from framework.framework import framework
  if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
    pygame.draw.rect(window.screen, color.silver, (100, 450, 150, 50))
    if click == (1, 0, 0):
     movementStrip()
     framework()
  else:
     pygame.draw.rect(window.screen, color.white, (100, 450, 150, 50))
  Buttons.createButton(window.screen,100, 450, 150, 50,"CONTINUE")  
  