from tkinter.tix import Form
import pygame
import sys
import movementBus

class main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana");
    numberOfYellowStripImg=7
    mouse=pygame.mouse.get_pos()
    cont=0
    stopCont=0
    stationStop=0
    acceleration=1
    numberImg=1
    personCont=0
    movPerson=1
    pauseMov=0
   
  
def timeMovement():
    clock= pygame.time.Clock()
    clock.tick(100)
  
movementBus.framework()    
 
