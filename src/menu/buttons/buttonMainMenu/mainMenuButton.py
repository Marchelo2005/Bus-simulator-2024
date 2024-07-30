import pygame; from utils.constants.constantWindow.constantWindow import window
from movementBus.valueReset.valueReset import movement
from utils.constants.constantColor.constantColor import color; from menu.buttons.buttons import Buttons

def mainMenuButton(mouse,click):
  if 600 < mouse[0] < 750 and 450 < mouse[1] < 500:
    from menu.mainMenu.introLoop.introLoop import introLoop
    pygame.draw.rect(window.screen, color.silver, (600, 450, 150, 50))
    if click == (1, 0, 0):
      movement.restart()
      introLoop()
  else:
   pygame.draw.rect(window.screen, color.white, (600, 450, 150, 50))
  Buttons.createButton(window.screen,600, 450, 150, 50,"MAIN MENU")
 
