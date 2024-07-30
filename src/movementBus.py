import mysql.connector
from mysql.connector import Error
import pygame
import sys
import random

# Colores
white = (255, 255, 255)
silver = (192, 192, 192)
red = (255, 0, 0)  # Color del punto
points = [
    (175, 230), (196, 230), (197, 294), (172, 324), (195, 324),
    (174, 357), (195, 354), (172, 388), (196, 388),
    (172, 461), (196, 461), (172, 496), (197, 496), (221, 496),
    (245, 496), (267, 496), (266, 422), (244, 422), (265, 393),
    (243, 393), (266, 393), (244, 360), (266, 358), (267, 325),
    (243, 327), (266, 294), (243, 294), (266, 263), (243, 263),
    (266, 228)
]

# Variables globales
totalMoneyRaised = 0
drawn_points = []  # Lista para almacenar los puntos dibujados
occupied_seats = set()
MAX_CAPACITY = 30  # Capacidad máxima del autobús
FARE = 0.35  # Precio del pasaje

class MyClass:
    @staticmethod
    def create_connection():
        try:
            connection = mysql.connector.connect(
                host="mysql-esestrada.alwaysdata.net",
                user="esestrada_machel",
                passwd="W26y.yiJTxt!LLs",
                database="esestrada_simula"
            )
            return connection
        except Error as e:
            print(f"The error '{e}' occurred")
            return None

    @staticmethod
    def insert_record(totalMoney):
        totalPersons = totalMoney / FARE  # Calcular el total de personas
        connection = MyClass.create_connection()
        if connection:
            try:
                myCursor = connection.cursor()
                sql = "INSERT INTO ACCOUNTINGTWO (totalPersons, totalMoney) VALUES (%s, %s)"
                insertValues = (totalPersons, totalMoney)
                myCursor.execute(sql, insertValues)
                connection.commit()  # Confirmar la transacción
                print(myCursor.rowcount, "registro insertado")
            except Error as e:
                print(f"The error '{e}' occurred")
            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection is closed")

class movementBus:
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
    loadingPassengers = False  # Indicador de si el autobús está cargando pasajeros

def paused():
    # Pausa 
    instructionBackgroundtwo = pygame.image.load("interfaz2.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        movementBus.screen.blit(instructionBackgroundtwo, (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = text_objects("PAUSED", largeText)
        textRect.center = (400, 300)
        movementBus.screen.blit(textSurf, textRect)
        # FOR CONTINUE
        continueButton()
        # FOR RESTART
        restartButton()
        # FOR MAIN MENU
        mainMenuButton()

        pygame.display.update()

def continueButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
        pygame.draw.rect(movementBus.screen, silver, (100, 450, 150, 50))
        if click[0] == 1:
            framework()
    else:
        pygame.draw.rect(movementBus.screen, white, (100, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("CONTINUE", smallText)
    textRect.center = (175, 475)
    movementBus.screen.blit(textSurf, textRect)

def restartButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 350 < mouse[0] < 500 and 450 < mouse[1] < 500:
        pygame.draw.rect(movementBus.screen, silver, (350, 450, 150, 50))
        if click[0] == 1:
            restart()
            framework()
    else:
        pygame.draw.rect(movementBus.screen, white, (350, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("RESTART", smallText)
    textRect.center = (425, 475)
    movementBus.screen.blit(textSurf, textRect) 

def mainMenuButton():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 600 < mouse[0] < 750 and 450 < mouse[1] < 500:
        pygame.draw.rect(movementBus.screen, silver, (600, 450, 150, 50))
        if click[0] == 1:
            restart()
            from Bus_simulator_2024 import Main
            Main.introLoop()
    else:
        pygame.draw.rect(movementBus.screen, white, (600, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("MAIN MENU", smallText)
    textRect.center = (675, 475)
    movementBus.screen.blit(textSurf, textRect)   

def restart():
    global drawn_points, occupied_seats, totalMoneyRaised
    drawn_points = []
    occupied_seats = set()
    totalMoneyRaised = 0 
    movementBus.cont, movementBus.stopCont, movementBus.stationStop, movementBus.personCont, movementBus.pauseMov = 0, 0, 0, 0, 0
    movementBus.acceleration, movementBus.numberImg, movementBus.movPerson = 1, 1, 1

def fund():
    font = pygame.font.SysFont(None, 20)
    moneyCollected = font.render(f"Total money raised: {totalMoneyRaised:.2f}", True, (0, 0, 0))
    maximumCapacity = font.render("Maximum capacity 30", True, (0, 0, 0))
    Totalstations = font.render("Total stations 10", True, (0, 0, 0))
    passengers = font.render(f"Passengers: {len(drawn_points)}", True, (0, 0, 0))
    movementBus.screen.blit(moneyCollected, (460, 25))
    movementBus.screen.blit(maximumCapacity, (460, 75))
    movementBus.screen.blit(Totalstations, (460, 90))
    movementBus.screen.blit(passengers, (460, 125))

def busPositioning(x, y):
    busImg = pygame.image.load("staffBus.png")
    busInsideImg = pygame.image.load("busInside.png")
    movementBus.screen.blit(busImg, (700, 200))
    movementBus.screen.blit(busInsideImg, (100, 50))

def movementStrip():
    global totalMoneyRaised 
    floortextureImg = pygame.image.load("grass.png")
    stripImg = pygame.image.load("strip.jpg")
    yellowStripImg = pygame.image.load("yellow_strip.jpg")
    stopImg = pygame.image.load("stop.png")
    person = pygame.image.load("persprue.png")
    rel_y = movementBus.numberOfYellowStripImg % 103
    if movementBus.numberImg == 11:
        MyClass.insert_record(totalMoneyRaised)
        restart()
        from Bus_simulator_2024 import Main
        Main.introLoop()
    else:
        recreoStopImg = pygame.image.load("shutdown" + repr(movementBus.numberImg) + ".png")
        movementBus.screen.blit(floortextureImg, (0, rel_y - 103))
        movementBus.screen.blit(floortextureImg, (700, rel_y - 103))
        movementBus.cont += 1
    if rel_y < 800:
        movementBus.screen.blit(floortextureImg, (0, rel_y))
        movementBus.screen.blit(floortextureImg, (700, rel_y))
        movementBus.screen.blit(yellowStripImg, (400, rel_y))
        movementBus.screen.blit(yellowStripImg, (400, rel_y + 100))
        movementBus.screen.blit(yellowStripImg, (400, rel_y + 200))
        movementBus.screen.blit(yellowStripImg, (400, rel_y + 300))
        movementBus.screen.blit(yellowStripImg, (400, rel_y + 400))
        movementBus.screen.blit(yellowStripImg, (400, rel_y + 500))
        movementBus.screen.blit(yellowStripImg, (400, rel_y - 100))
        movementBus.screen.blit(stripImg, (130, rel_y - 300))
        movementBus.screen.blit(stripImg, (130, rel_y + 20))
        movementBus.screen.blit(stripImg, (130, rel_y + 30))
        movementBus.screen.blit(stripImg, (670, rel_y - 300))
        movementBus.screen.blit(stripImg, (670, rel_y + 20))
        movementBus.screen.blit(stripImg, (670, rel_y + 30))
        if movementBus.cont > 1000 and (movementBus.stopCont % 800 - 200) < 580:
            movementBus.stopCont += movementBus.acceleration
            movementBus.screen.blit(stopImg, (0, movementBus.stopCont % 800 - 200))

        if (movementBus.stopCont % 800 - 200) > -80 and (movementBus.stationStop % 800 - 200) < 580:
            movementBus.stationStop += movementBus.acceleration
            movementBus.screen.blit(recreoStopImg, (0, movementBus.stationStop % 800 - 200))

        if movementBus.acceleration > 0:
            if (movementBus.stationStop % 800 - 200) > 0 and (movementBus.personCont % 800 - 200) < 45:
                movementBus.personCont += movementBus.acceleration
                movementBus.screen.blit(person, (60, movementBus.personCont - 10))
                movementBus.pauseMov = 0
        else:
            if movementBus.pauseMov < 40 and len(occupied_seats) < MAX_CAPACITY:
                movementBus.personCont += movementBus.movPerson
                movementBus.screen.blit(person, (movementBus.personCont % 150, 236))
                movementBus.pauseMov += 1
                if movementBus.pauseMov == 40 and len(occupied_seats) < MAX_CAPACITY:
                    for _ in range(1, random.randint(1, 12)):
                        from faceDetector import detector
                        detector.txtVideo = "person"
                        detector.face()
                        totalMoneyRaised += FARE  # pasaje
                        pygame.display.set_mode(movementBus.size)
                        pygame.display.set_caption("Ventana")
                        drawPoint(points)
                        movementBus.positionOfOutputMovement = 135
                        movementBus.orderMovement = False
            else:
                if len(occupied_seats) == MAX_CAPACITY:
                    probabilityOfPeopleDrop = random.randint(0, 1)
                    movementBus.positionOfOutputMovement -= 1
                    if movementBus.positionOfOutputMovement == 50 and movementBus.numberImg > 1 and probabilityOfPeopleDrop == 0:
                        from faceDetector import detector
                        detector.txtVideo = "exit"
                        detector.face()
                        deletePoints()
                        pygame.display.set_mode(movementBus.size)
                        pygame.display.set_caption("Ventana")
                        movementBus.orderMovement = True
                    if 0 < movementBus.positionOfOutputMovement < 50 and movementBus.orderMovement:
                        movementBus.screen.blit(person, (movementBus.positionOfOutputMovement % 135, 416))

        movementBus.numberOfYellowStripImg += movementBus.acceleration
        if movementBus.cont <= 583:
            if movementBus.cont % 53 == 0:
                if movementBus.acceleration <= 11:
                    movementBus.acceleration += 1
        else:
            if movementBus.cont % 53 == 0 and movementBus.cont <= 1219:
                movementBus.acceleration -= 1

        if movementBus.cont > 1200 and movementBus.cont > 2000:
            if movementBus.cont % 53 == 0:
                if movementBus.acceleration <= 11:
                    movementBus.acceleration += 1

        if movementBus.cont == 2200:
            movementBus.stopCont = 0
            movementBus.personCont = 0
            movementBus.stationStop = 0
            movementBus.numberImg += 1
            movementBus.cont = 0

def drawPoint(points):
    available_seats = [point for point in points if point not in occupied_seats]
    if available_seats:
        point = random.choice(available_seats)
        drawn_points.append(point)
        occupied_seats.add(point)
        pygame.draw.circle(movementBus.screen, red, point, 5)

def redrawPoints():
    for point in drawn_points:
        pygame.draw.circle(movementBus.screen, red, point, 5)

def deletePoints():
    if drawn_points:
        point = drawn_points.pop(random.randint(0, len(drawn_points) - 1))
        occupied_seats.remove(point)

def text_objects(text, font):
    # Función para renderizar texto
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
        movementBus.screen.fill((119, 119, 119))
        movementBus.mouse = pygame.mouse.get_pos()
        fund()
        busPositioning(0, 0)
        movementStrip()
        redrawPoints()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
            pygame.draw.rect(movementBus.screen, silver, (650, 0, 150, 50))
            if click[0] == 1:
                paused()
        else:
            pygame.draw.rect(movementBus.screen, white, (650, 0, 150, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("PAUSE", smallText)
        textRect.center = (725, 25)
        movementBus.screen.blit(textSurf, textRect)
        pygame.display.flip()

framework()
