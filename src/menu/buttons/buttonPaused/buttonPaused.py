import pygame; from utils.constants.constantColor.constantColor import color
from utils.constants.constantWindow.constantWindow import window; from menu.mainMenu.pause.paused import paused
from menu.buttons.buttons import Buttons

def buttonPaused(mouse,click):
 if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
  pygame.draw.rect(window.screen, color.silver, (650, 0, 150, 50))
  if click == (1, 0, 0): 
   paused()
  else:
   pygame.draw.rect(window.screen, color.white, (650, 0, 150, 50))
  Buttons.createButton(window.screen,650, 0, 150, 50,"PAUSE")
