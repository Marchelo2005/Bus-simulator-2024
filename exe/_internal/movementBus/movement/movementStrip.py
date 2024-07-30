import pygame
from movementBus.imgEnvironment.img import environment
from utils.constants.constantWindow.constantWindow import window

def movementStrip():
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y + 100))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y + 200))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y + 300))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y + 400))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y + 500))
    window.screen.blit(environment.yellowStripImg,  (400, window.rel_y - 100))
    window.screen.blit(environment.stripImg, (130, window.rel_y - 300))
    window.screen.blit(environment.stripImg, (130, window.rel_y + 20))
    window.screen.blit(environment.stripImg, (130, window.rel_y + 30))
    window.screen.blit(environment.stripImg, (670, window.rel_y - 300))
    window.screen.blit(environment.stripImg, (670, window.rel_y + 20))
    window.screen.blit(environment.stripImg, (670, window.rel_y + 30))
   