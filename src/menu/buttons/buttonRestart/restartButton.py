import pygame; from utils.constants.constantWindow.constantWindow import window
from movementBus.valueReset.valueReset import movement
from utils.constants.constantColor.constantColor import color; from menu.buttons.buttons import Buttons

def restartButton(mouse,click):
 from framework.framework import framework
 if 350 < mouse[0] < 500 and 450 < mouse[1] < 500:
   pygame.draw.rect(window.screen, color.silver, (350, 450, 150, 50))
   if click == (1, 0, 0):
    movement.restart()
    framework()
 else:
   pygame.draw.rect(window.screen, color.white, (350, 450, 150, 50))
 Buttons.createButton(window.screen,350, 450, 150, 50,"RESTART")  

