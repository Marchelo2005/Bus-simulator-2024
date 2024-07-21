import pygame
import sys
from ui.ui_elements import handle_pause_button, fund, busPositioning
from game.game_logic import movementStrip, redrawPoints

# Colores
white = (255, 255, 255)
silver = (192, 192, 192)

class Main:
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana")
    
    @staticmethod
    def intro_loop():
        introImage = pygame.image.load("assets/PORTADA1.png")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            Main.screen.blit(introImage, (0, 0))  
            
            pygame.draw.rect(Main.screen, white, (80, 280, 150, 50))
            pygame.draw.rect(Main.screen, white, (327, 280, 165, 50))
            pygame.draw.rect(Main.screen, white, (580, 280, 150, 50))
            Main.buttons()

            smallText = pygame.font.Font("freesansbold.ttf", 20)
            textSurface, textRect = Main.text_object("CLOSE", smallText)
            textRect.center = ((580 + (150 / 2)), (280 + (50 / 2)))
            Main.screen.blit(textSurface, textRect)

            pygame.display.update()

    @staticmethod
    def instruction():
        instructionBackground = pygame.image.load("assets/intruction1.png")
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()

            Main.screen.blit(instructionBackground, (0, 0))

            pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 580 < mouse[0] < 730 and 300 < mouse[1] < 350:
                pygame.draw.rect(Main.screen, silver, (650, 5, 150, 50))
            else:
                pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))

            smallText = pygame.font.Font("freesansbold.ttf", 20)
            textSurface, textRect = Main.text_object("BACK", smallText)
            textRect.center = (650 + (150 / 2), 5 + (50 / 2))
            Main.screen.blit(textSurface, textRect)

            if click == (1, 0, 0):
                Main.intro_loop()

            pygame.display.update()
            clock.tick(30)

    @staticmethod
    def text_object(text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    @staticmethod
    def buttons():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 80 < mouse[0] < 230 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (80, 280, 150, 50))
            if click == (1, 0, 0):
                from game.movement_bus import framework
                framework()        
        else:
            pygame.draw.rect(Main.screen, white, (80, 280, 150, 50)) 

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.text_object("START", smallText)
        textRect.center = ((80 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 336 < mouse[0] < 485 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (327, 280, 165, 50))
            if click == (1, 0, 0):
                Main.instruction()
        else:
            pygame.draw.rect(Main.screen, white, (327, 280, 165, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.text_object("INTRODUCTION", smallText)
        textRect.center = ((336 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 580 < mouse[0] < 730 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (580, 280, 150, 50))
            if click == (1, 0, 0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(Main.screen, white, (580, 280, 150, 50))   

Main.intro_loop()
