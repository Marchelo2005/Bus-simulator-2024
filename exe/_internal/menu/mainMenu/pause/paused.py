import pygame; import sys 
from utils.constants.constantWindow.constantWindow import window; from menu.buttons.buttons import Buttons
from menu.buttons.buttonContinue.continueButton import continueButton; from menu.buttons.buttonMainMenu.mainMenuButton import mainMenuButton 
from menu.buttons.buttonRestart.restartButton import restartButton

def paused():
    instructionBackgroundtwo=pygame.image.load("assets/assetsInterface/interfaz2.png")
    while True:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.screen.blit(instructionBackgroundtwo, (0, 0))
        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = Buttons.textObjects("PAUSED", largeText)
        textRect.center = (400, 300)
        window.screen.blit(textSurf, textRect)
        continueButton(mouse,click)
        restartButton(mouse,click)
        mainMenuButton(mouse,click)
        pygame.display.update()
