import pygame,sys
from movementBus.pointsAndVideos.drawPoint.redrawPoints import redrawPoints; from utils.constants.constantWindow.constantWindow import window
from movementBus.positioning.busPositioning import busPositioning; from movementBus.movementBus import movementBus
from menu.mainMenu.pause.paused import paused; from menu.buttons.buttonPaused.buttonPaused import buttonPaused
from menu.buttons.buttons import Buttons; from utils.constants.constantColor.constantColor import color; from utils.fund.fund import fund

def framework(): 
 while True:
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()    
   if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_p:  
     paused()
  window.screen.fill((119, 119, 119))
  fund()
  busPositioning()
  movementBus()
  redrawPoints()
  Buttons.buttonDrawing(window.screen, color.white, 650, 0, 150, 50)
  buttonPaused(mouse,click)
  pygame.display.flip()
  