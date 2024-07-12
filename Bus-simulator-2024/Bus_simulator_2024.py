import pygame
import sys
import movementBus

# colores
white = (255, 255, 255)
silver = (192, 192, 192)
red = (255, 0, 0)  # color del punto

class Main:
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana")
    
    def introLoop():
     # Loop de introducción 
     introImage = pygame.image.load("PORTADA1.png")
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

        # Función de los botones
        Main.buttons()

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.textObject("CLOSE", smallText)
        textRect.center = ((580 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        pygame.display.update()

    def instruction():
     instructionBackground = pygame.image.load("intruction1.png")
     clock = pygame.time.Clock()
     while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        Main.screen.blit(instructionBackground, (0, 0))

        largetext = pygame.font.Font("freesansbold.ttf", 80)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)

        pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 580 < mouse[0] < 730 and 300 < mouse[1] < 350:
            pygame.draw.rect(Main.screen, silver, (650, 5, 150, 50))
        else:
            pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.textObject("BACK", smallText)
        textRect.center = (650 + (150 / 2), 5 + (50 / 2))
        Main.screen.blit(textSurface, textRect)

        if click == (1, 0, 0):
            Main.introLoop()

        pygame.display.update()
        clock.tick(30)

    def textObject(text, font):
     # Función para renderizar texto
     textSurface = font.render(text, True, (0, 0, 0))
     return textSurface, textSurface.get_rect()

# Dibujar los puntos
    def draw_point(points):
     points = [
        (175, 230), (196, 230), (175, 294), (197, 294), (172, 324),
        (195, 324), (174, 357), (195, 354), (172, 388), (196, 388),
        (172, 461), (196, 461), (172, 496), (197, 496), (221, 496),
        (245, 496), (267, 496), (266, 422), (244, 422), (265, 393),
        (243, 393), (266, 393), (244, 360), (266, 358), (243, 357),
        (267, 325), (243, 327), (265, 325), (266, 294), (243, 294),
        (266, 263), (243, 263), (266, 228)
    ]
     for point in points:
        pygame.draw.circle(Main.screen, red, point, 5)
        
    def buttons():
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 80 < mouse[0] < 230 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (80, 280, 150, 50))
            if click == (1, 0, 0):
                movementBus.framework()
        else:
            pygame.draw.rect(Main.screen, white, (80, 280, 150, 50)) 

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.textObject("START", smallText)
        textRect.center = ((80 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 336 < mouse[0] < 485 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (327, 280, 165, 50))
            if click == (1, 0, 0):
                Main.instruction()
        else:
            pygame.draw.rect(Main.screen, white, (327, 280, 165, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = Main.textObject("INTRODUCTION", smallText)
        textRect.center = ((336 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 580 < mouse[0] < 730 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (580, 280, 150, 50))
            if click == (1, 0, 0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(Main.screen, white, (580, 280, 150, 50))   
                    
Main.introLoop()

