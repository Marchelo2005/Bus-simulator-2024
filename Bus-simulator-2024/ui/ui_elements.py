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

def continueButton(screen):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
        pygame.draw.rect(screen, silver, (100, 450, 150, 50))
        if click == (1, 0, 0):
            from game.movement_bus import movementStrip, framework
            movementStrip(screen)
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
            from game.movement_bus import restart, framework
            restart()
            framework()
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
            from game.movement_bus import restart
            restart()
            from ui.main_menu import Main
            Main.intro_loop()
    else:
        pygame.draw.rect(screen, white, (600, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("MAIN MENU", smallText)
    textRect.center = (675, 475)
    screen.blit(textSurf, textRect)

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

def busPositioning(screen):
    busImg = pygame.image.load("assets/staffBus.png")
    busInsideImg = pygame.image.load("assets/busInside.png")
    screen.blit(busImg, (700, 200))
    screen.blit(busInsideImg, (100, 50))

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
