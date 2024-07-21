import pygame
import random
from utils.constants import points, red
from utils.face_detector import Detector
from ui.ui_elements import paused, fund, busPositioning, continueButton, restartButton, mainMenuButton

# Colores
white = (255, 255, 255)
silver = (192, 192, 192)

class MovementBus:
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana")
    numberOfYellowStripImg = 7
    cont, stopCont, stationStop, personCont, pauseMov = 0, 0, 0, 0, 0
    acceleration, numberImg, movPerson = 1, 1, 1
    positionOfOutputMovement = 135
    orderMovement = False
    randomValidator = True

totalMoneyRaised = 0
drawn_points = []

def paused():
    instructionBackgroundtwo = pygame.image.load("assets/interfaz2.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        MovementBus.screen.blit(instructionBackgroundtwo, (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = text_objects("PAUSED", largeText)
        textRect.center = (400, 300)
        MovementBus.screen.blit(textSurf, textRect)
        continueButton(MovementBus.screen)
        restartButton(MovementBus.screen)
        mainMenuButton(MovementBus.screen)
        pygame.display.update()

def restart():
    global drawn_points
    drawn_points = []
    MovementBus.cont, MovementBus.stopCont, MovementBus.stationStop, MovementBus.personCont, MovementBus.pauseMov = 0, 0, 0, 0, 0
    MovementBus.acceleration, MovementBus.numberImg, MovementBus.movPerson = 1, 1, 1

def movementStrip():
    global totalMoneyRaised
    floortextureImg = pygame.image.load("assets/grass.png")
    stripImg = pygame.image.load("assets/strip.jpg")
    yellowStripImg = pygame.image.load("assets/yellow_strip.jpg")
    stopImg = pygame.image.load("assets/stop.png")
    person = pygame.image.load("assets/persprue.png")
    rel_y = MovementBus.numberOfYellowStripImg % 103
    if MovementBus.numberImg == 11:
        restart()
        from ui.main_menu import Main
        Main.intro_loop()
    else:
        recreoStopImg = pygame.image.load(f"assets/shutdown{MovementBus.numberImg}.png")
        MovementBus.screen.blit(floortextureImg, (0, rel_y - 103))
        MovementBus.screen.blit(floortextureImg, (700, rel_y - 103))
        MovementBus.cont += 1
    if rel_y < 800:
        MovementBus.screen.blit(floortextureImg, (0, rel_y))
        MovementBus.screen.blit(floortextureImg, (700, rel_y))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y + 100))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y + 200))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y + 300))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y + 400))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y + 500))
        MovementBus.screen.blit(yellowStripImg, (400, rel_y - 100))
        MovementBus.screen.blit(stripImg, (130, rel_y - 300))
        MovementBus.screen.blit(stripImg, (130, rel_y + 20))
        MovementBus.screen.blit(stripImg, (130, rel_y + 30))
        MovementBus.screen.blit(stripImg, (670, rel_y - 300))
        MovementBus.screen.blit(stripImg, (670, rel_y + 20))
        MovementBus.screen.blit(stripImg, (670, rel_y + 30))
        if MovementBus.cont > 1000 and (MovementBus.stopCont % 800 - 200) < 580:
            MovementBus.stopCont += MovementBus.acceleration
            MovementBus.screen.blit(stopImg, (0, MovementBus.stopCont % 800 - 200))

        if (MovementBus.stopCont % 800 - 200) > -80 and (MovementBus.stationStop % 800 - 200) < 580:
            MovementBus.stationStop += MovementBus.acceleration
            MovementBus.screen.blit(recreoStopImg, (0, MovementBus.stationStop % 800 - 200))

        if MovementBus.acceleration > 0:
            if (MovementBus.stationStop % 800 - 200) > 0 and (MovementBus.personCont % 800 - 200) < 45:
                MovementBus.personCont += MovementBus.acceleration
                MovementBus.screen.blit(person, (60, MovementBus.personCont - 10))
                MovementBus.pauseMov = 0
        else:
            if MovementBus.pauseMov < 40:
                MovementBus.personCont += MovementBus.movPerson
                MovementBus.screen.blit(person, (MovementBus.personCont % 150, 236))
                MovementBus.pauseMov += 1
                if MovementBus.pauseMov == 40:
                    for numberRandomVideo in range(1, random.randint(1, 5), 1):
                        Detector.txtVideo = "person"
                        Detector.face()
                        totalMoneyRaised += 35  # pasaje
                        pygame.display.set_mode(MovementBus.size)
                        pygame.display.set_caption("Ventana")
                        drawPoint(points)
                        MovementBus.positionOfOutputMovement = 135
                        MovementBus.orderMovement = False
            else:
                probabilityOfPeopleDrop = random.randint(0, 1)
                MovementBus.positionOfOutputMovement -= 1
                if MovementBus.positionOfOutputMovement == 50 and MovementBus.numberImg > 1 and probabilityOfPeopleDrop == 0:
                    Detector.txtVideo = "exit"
                    Detector.face()
                    pygame.display.set_mode(MovementBus.size)
                    pygame.display.set_caption("Ventana")
                    MovementBus.orderMovement = True
                if MovementBus.positionOfOutputMovement > 0 and MovementBus.positionOfOutputMovement < 50 and MovementBus.orderMovement:
                    MovementBus.screen.blit(person, (MovementBus.positionOfOutputMovement % 135, 416))

        MovementBus.numberOfYellowStripImg += MovementBus.acceleration
        if MovementBus.cont <= 583:
            if MovementBus.cont % 53 == 0:
                if MovementBus.acceleration <= 11:
                    MovementBus.acceleration += 1
        else:
            if MovementBus.cont % 53 == 0 and MovementBus.cont <= 1219:
                MovementBus.acceleration -= 1

        if MovementBus.cont > 1400 and MovementBus.cont > 2200:
            if MovementBus.cont % 53 == 0:
                if MovementBus.acceleration <= 11:
                    MovementBus.acceleration += 1

        if MovementBus.cont == 2400:
            MovementBus.stopCont = 0
            MovementBus.personCont = 0
            MovementBus.stationStop = 0
            MovementBus.numberImg += 1
            MovementBus.cont = 0

def drawPoint(points):
    randomSeat = random.randint(0, 30)
    point = points[randomSeat]
    drawn_points.append(point)
    pygame.draw.circle(MovementBus.screen, red, point, 5)

def redrawPoints():
    for point in drawn_points:
        pygame.draw.circle(MovementBus.screen, red, point, 5)

def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def framework():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Presionar 'P' para pausar
                    paused()
        MovementBus.screen.fill((119, 119, 119))
        MovementBus.mouse = pygame.mouse.get_pos()
        fund()
        busPositioning()
        movementStrip()
        redrawPoints()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
            pygame.draw.rect(MovementBus.screen, silver, (650, 0, 150, 50))
            if click == (1, 0, 0):
                paused()
        else:
            pygame.draw.rect(MovementBus.screen, white, (650, 0, 150, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("PAUSE", smallText)
        textRect.center = (725, 25)
        MovementBus.screen.blit(textSurf, textRect)
        pygame.display.flip()
