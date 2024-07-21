# En el archivo ui/buttons.py
import pygame
from utils.constants import white, silver

def continueButton(screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
        pygame.draw.rect(screen, silver, (100, 450, 150, 50))
        if click == (1, 0, 0):
            movementStrip()
            framework()
    else:
        pygame.draw.rect(screen, white, (100, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("CONTINUE", smallText)
    textRect.center = (175, 475)
    screen.blit(textSurf, textRect)

def restartButton(screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 350 < mouse[0] < 500 and 450 < mouse[1] < 500:
        pygame.draw.rect(screen, silver, (350, 450, 150, 50))
        if click == (1, 0, 0):
            restart()
            framework()
            # Aquí puedes reiniciar tu juego
    else:
        pygame.draw.rect(screen, white, (350, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("RESTART", smallText)
    textRect.center = (425, 475)
    screen.blit(textSurf, textRect)

def mainMenuButton(screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 600 < mouse[0] < 750 and 450 < mouse[1] < 500:
        pygame.draw.rect(screen, silver, (600, 450, 150, 50))
        if click == (1, 0, 0):
            restart()
            from Bus_simulator_2024 import Main
            Main.introLoop()
    else:
        pygame.draw.rect(screen, white, (600, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("MAIN MENU", smallText)
    textRect.center = (675, 475)
    screen.blit(textSurf, textRect)

def handle_pause_button(screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
        pygame.draw.rect(screen, silver, (650, 0, 150, 50))
        if click == (1, 0, 0):
            paused(screen)
    else:
        pygame.draw.rect(screen, white, (650, 0, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("PAUSE", smallText)
    textRect.center = (725, 25)
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

