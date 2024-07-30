import pygame
from utils.constants.constantWindow.constantWindow import window

def busPositioning():
 busImg=pygame.image.load("assets/assetsBus/staffBus.png")
 busInsideImg=pygame.image.load("assets/assetsBus/busInside.png")
 window.screen.blit(busImg,(700,200))  
 window.screen.blit(busInsideImg,(100,50)) 

