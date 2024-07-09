import pygame
import sys

# colores
white = (255, 255, 255)
silver = (192, 192, 192)
red = (255, 0, 0)  # color del punto

class Main:
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana")
    numberOfYellowStripImg = 7

    # se agregó la interfaz
    intro_image = pygame.image.load("PORTADA1.png")
    instruction_background = pygame.image.load("intruction1.png")

    # agregar punto
    points = [
        (175, 230), (196, 230), (175, 294), (197, 294), (172, 324),
        (195, 324), (174, 357), (195, 354), (172, 388), (196, 388),
        (172, 461), (196, 461), (172, 496), (197, 496), (221, 496),
        (245, 496), (267, 496), (266, 422), (244, 422), (265, 393),
        (243, 393), (266, 393), (244, 360), (266, 358), (243, 357),
        (267, 325), (243, 327), (265, 325), (266, 294), (243, 294),
        (266, 263), (243, 263), (266, 228)
    ]

def intro_loop():
    # Loop de introducción 
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        Main.screen.blit(Main.intro_image, (0, 0))  

        pygame.draw.rect(Main.screen, white, (80, 280, 150, 50))
        pygame.draw.rect(Main.screen, white, (327, 280, 165, 50))
        pygame.draw.rect(Main.screen, white, (580, 280, 150, 50))

        # Función de los botones
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 80 < mouse[0] < 230 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (80, 280, 150, 50))
            if click == (1, 0, 0):
                framework()
        else:
            pygame.draw.rect(Main.screen, white, (80, 280, 150, 50)) 

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_objects("START", smallText)
        textRect.center = ((80 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 336 < mouse[0] < 485 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (327, 280, 165, 50))
            if click == (1, 0, 0):
                instruction()
        else:
            pygame.draw.rect(Main.screen, white, (327, 280, 165, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_objects("INTRODUCTION", smallText)
        textRect.center = ((336 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        if 580 < mouse[0] < 730 and 280 < mouse[1] < 330:
            pygame.draw.rect(Main.screen, silver, (580, 280, 150, 50))
            if click == (1, 0, 0):
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(Main.screen, white, (580, 280, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_objects("CLOSE", smallText)
        textRect.center = ((580 + (150 / 2)), (280 + (50 / 2)))
        Main.screen.blit(textSurface, textRect)

        pygame.display.update()

def instruction():
    # Loop de instrucciones
    instruction = True
    clock = pygame.time.Clock()
    while instruction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        Main.screen.blit(Main.instruction_background, (0, 0))

        largetext = pygame.font.Font("freesansbold.ttf", 80)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)

        pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))

        mouse = pygame.mouse.get_pos()
        if 580 < mouse[0] < 730 and 300 < mouse[1] < 350:
            pygame.draw.rect(Main.screen, silver, (650, 5, 150, 50))
        else:
            pygame.draw.rect(Main.screen, white, (650, 5, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurface, textRect = text_objects("BACK", smallText)
        textRect.center = (650 + (150 / 2), 5 + (50 / 2))
        Main.screen.blit(textSurface, textRect)

        click = pygame.mouse.get_pressed()
        if click == (1, 0, 0):
            intro_loop()

        pygame.display.update()
        clock.tick(30)

def text_objects(text, font):
    # Función para renderizar texto
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def timeMovement():
    # Control del tiempo
    clock = pygame.time.Clock()
    clock.tick(100)

def fund():
    # Función para mostrar fondo y elementos estáticos
    font = pygame.font.SysFont(None, 20) 
    floortextureImg = pygame.image.load("grass.jpeg")
    stripImg = pygame.image.load("strip.jpg")
    yellowStripImg = pygame.image.load("yellow_strip.jpg")

    Main.screen.blit(floortextureImg, (-150, 0))
    Main.screen.blit(floortextureImg, (700, 0))
    Main.screen.blit(yellowStripImg, (400, 0))
    Main.screen.blit(yellowStripImg, (400, 100))
    Main.screen.blit(yellowStripImg, (400, 200))
    Main.screen.blit(yellowStripImg, (400, 300))
    Main.screen.blit(yellowStripImg, (400, 400))
    Main.screen.blit(yellowStripImg, (400, 500))
    Main.screen.blit(yellowStripImg, (400, 600))
    Main.screen.blit(stripImg, (130, 0))
    Main.screen.blit(stripImg, (670, 0))

    moneyCollected = font.render("Money collected", True, (255, 255, 255))
    maximumCapacity = font.render("Maximum capacity", True, (0, 0, 0))
    passengers = font.render("Passengers", True, (0, 0, 0))
    Main.screen.blit(moneyCollected, (460, 25))
    Main.screen.blit(maximumCapacity, (460, 75))
    Main.screen.blit(passengers, (460, 125)) 

def paused():
    # Pausa del juego
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        Main.screen.blit(Main.instruction_background, (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = text_objects("PAUSED", largeText)
        textRect.center = (400, 300)
        Main.screen.blit(textSurf, textRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # FOR CONTINUE
        if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
            pygame.draw.rect(Main.screen, silver, (100, 450, 150, 50))
            if click == (1, 0, 0):
                pause = False
        else:
            pygame.draw.rect(Main.screen, white, (100, 450, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("CONTINUE", smallText)
        textRect.center = (175, 475)
        Main.screen.blit(textSurf, textRect)

        # FOR RESTART
        if 350 < mouse[0] < 500 and 450 < mouse[1] < 500:
            pygame.draw.rect(Main.screen, silver, (350, 450, 150, 50))
            if click == (1, 0, 0):
                intro_loop()  # Aquí puedes reiniciar tu juego
        else:
            pygame.draw.rect(Main.screen, white, (350, 450, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("RESTART", smallText)
        textRect.center = (425, 475)
        Main.screen.blit(textSurf, textRect)

        # FOR MAIN MENU
        if 600 < mouse[0] < 750 and 450 < mouse[1] < 500:
            pygame.draw.rect(Main.screen, silver, (600, 450, 150, 50))
            if click == (1, 0, 0):
                intro_loop()
        else:
            pygame.draw.rect(Main.screen, white, (600, 450, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("MAIN MENU", smallText)
        textRect.center = (675, 475)
        Main.screen.blit(textSurf, textRect)

        pygame.display.update()

def movementStrip():
    floortextureImg = pygame.image.load("grass.jpeg")
    stripImg = pygame.image.load("strip.jpg")
    yellowStripImg = pygame.image.load("yellow_strip.jpg")
    rel_y = Main.numberOfYellowStripImg % floortextureImg.get_rect().width
    Main.screen.blit(yellowStripImg, (-150, rel_y - floortextureImg.get_rect().width))
    Main.screen.blit(yellowStripImg, (700, rel_y - floortextureImg.get_rect().width))
    if rel_y < 800:
        Main.screen.blit(floortextureImg, (-150, rel_y))
        Main.screen.blit(floortextureImg, (700, rel_y))
        Main.screen.blit(yellowStripImg, (400, rel_y))
        Main.screen.blit(yellowStripImg, (400, rel_y + 100))
        Main.screen.blit(yellowStripImg, (400, rel_y + 200))
        Main.screen.blit(yellowStripImg, (400, rel_y + 300))
        Main.screen.blit(yellowStripImg, (400, rel_y + 400))
        Main.screen.blit(yellowStripImg, (400, rel_y + 500))
        Main.screen.blit(yellowStripImg, (400, rel_y - 100))
        Main.screen.blit(stripImg, (130, rel_y - 200))
        Main.screen.blit(stripImg, (130, rel_y + 20))
        Main.screen.blit(stripImg, (130, rel_y + 30))
        Main.screen.blit(stripImg, (670, rel_y - 100))
        Main.screen.blit(stripImg, (670, rel_y + 20))
        Main.screen.blit(stripImg, (670, rel_y + 30))
        Main.numberOfYellowStripImg += 7 

def busPositioning(x, y):
    # Posicionamiento del bus
    busImg = pygame.image.load("staffBus.png")
    busInsideImg = pygame.image.load("busInside.png")
    Main.screen.blit(busImg, (700, 200))  
    Main.screen.blit(busInsideImg, (100, 50)) 

# Dibujar los puntos
def draw_points(points):
    for point in points:
        pygame.draw.circle(Main.screen, red, point, 5)

def framework():
    # Framework principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Presionar 'P' para pausar
                    paused()
        Main.screen.fill((119, 119, 119))
        fund()
        busPositioning(0, 0)
        draw_points(Main.points)  # Coordenadas del punto rojo
        pygame.draw.rect(Main.screen, white, (650, 0, 150, 50))

        mouse = pygame.mouse.get_pos()
        if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
            pygame.draw.rect(Main.screen, silver, (650, 0, 150, 50))
        else:
            pygame.draw.rect(Main.screen, white, (650, 0, 150, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("PAUSE", smallText)
        textRect.center = (725, 25)
        Main.screen.blit(textSurf, textRect)

        pygame.display.flip()

intro_loop()
