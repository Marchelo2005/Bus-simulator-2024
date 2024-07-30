
# En el archivo ui/screens.py
import pygame
import sys
from utils.constants import white, silver

def paused(screen):
    instructionBackgroundtwo = pygame.image.load("assets/interfaz2.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        screen.blit(instructionBackgroundtwo, (0, 0))
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = text_objects("PAUSED", largeText)
        textRect.center = (400, 300)
        screen.blit(textSurf, textRect)
        continueButton(screen)
        restartButton(screen)
        mainMenuButton(screen)
        pygame.display.update()

def fund(screen, totalMoneyRaised):
    font = pygame.font.SysFont(None, 20)
    moneyCollected = font.render(f"Total money raised: {totalMoneyRaised:.1f}", True, (0, 0, 0))
    maximumCapacity = font.render("Maximum capacity 30", True, (0, 0, 0))
    Totalstations = font.render("Total stations 10", True, (0, 0, 0))
    passengers = font.render("Passengers", True, (0, 0, 0))
    screen.blit(moneyCollected, (460, 25))
    screen.blit(maximumCapacity, (460, 75))
    screen.blit(Totalstations, (460, 90))
    screen.blit(passengers, (460, 125))

def busPositioning(screen, x, y):
    busImg = pygame.image.load("assets/staffBus.png")
    busInsideImg = pygame.image.load("assets/busInside.png")
    screen.blit(busImg, (700, 200))
    screen.blit(busInsideImg, (100, 50))
