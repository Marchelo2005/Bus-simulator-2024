import pygame
from utils.constants.constantWindow.constantWindow import window
from utils.constants.constantColor.constantColor import color
from menu.buttons.buttons import Buttons
def Close(mouse,click):
 if 580 < mouse[0] < 730 and 280 < mouse[1] < 330:
  pygame.draw.rect(window.screen, color.silver, (580, 280, 150, 50))
  if click == (1, 0, 0):
   pygame.quit()
   quit()
 else:
  pygame.draw.rect(window.screen, color.white, (580, 280, 150, 50))   
 Buttons.createButton(window.screen,580, 280, 150, 50,"CLOSE")