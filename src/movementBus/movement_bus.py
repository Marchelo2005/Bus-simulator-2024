import mysql.connector
from mysql.connector import Error
import pygame
import sys
import random
from  import detector

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
        totalPersons = totalMoney / FARE
        connection = MyClass.create_connection()
        if connection:
            try:
                myCursor = connection.cursor()
                sql = "INSERT INTO ACCOUNTINGTWO (totalPersons, totalMoney) VALUES (%s, %s)"
                insertValues = (totalPersons, totalMoney)
                myCursor.execute(sql, insertValues)
                connection.commit()
                print(myCursor.rowcount, "registro insertado")
            except Error as e:
                print(f"The error '{e}' occurred")
            finally:
                if connection.is_connected():
                    connection.close()
                    print("MySQL connection is closed")

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
    loadingPassengers = False  # Indicador de si el autobús está cargando pasajeros

def paused():
    instructionBackgroundtwo = pygame.image.load("interfaz2.png")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        MovementBus.screen.blit(instructionBackgroundtwo, (0, 0))

        largeText = pygame.font.Font("freesansbold.ttf", 115)
        textSurf, textRect = text_objects("PAUSED", largeText)
        textRect.center = (400, 300)
        MovementBus.screen.blit(textSurf, textRect)
        continue_button()
        restart_button()
        main_menu_button()

        pygame.display.update()

def continue_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 100 < mouse[0] < 250 and 450 < mouse[1] < 500:
        pygame.draw.rect(MovementBus.screen, silver, (100, 450, 150, 50))
        if click[0] == 1:
            framework()
    else:
        pygame.draw.rect(MovementBus.screen, white, (100, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("CONTINUE", smallText)
    textRect.center = (175, 475)
    MovementBus.screen.blit(textSurf, textRect)

def restart_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 350 < mouse[0] < 500 and 450 < mouse[1] < 500:
        pygame.draw.rect(MovementBus.screen, silver, (350, 450, 150, 50))
        if click[0] == 1:
            restart()
            framework()
    else:
        pygame.draw.rect(MovementBus.screen, white, (350, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("RESTART", smallText)
    textRect.center = (425, 475)
    MovementBus.screen.blit(textSurf, textRect)

def main_menu_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 600 < mouse[0] < 750 and 450 < mouse[1] < 500:
        pygame.draw.rect(MovementBus.screen, silver, (600, 450, 150, 50))
        if click[0] == 1:
            restart()
            from game.game_logic import Main
            Main.intro_loop()
    else:
        pygame.draw.rect(MovementBus.screen, white, (600, 450, 150, 50))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("MAIN MENU", smallText)
    textRect.center = (675, 475)
    MovementBus.screen.blit(textSurf, textRect)

def restart():
    global drawn_points, occupied_seats, totalMoneyRaised
    drawn_points = []
    occupied_seats = set()
    totalMoneyRaised = 0 
    MovementBus.cont, MovementBus.stopCont, MovementBus.stationStop, MovementBus.personCont, MovementBus.pauseMov = 0, 0, 0, 0, 0
    MovementBus.acceleration, MovementBus.numberImg, MovementBus.movPerson = 1, 1, 1

def fund():
    font = pygame.font.SysFont(None, 20)
    moneyCollected = font.render(f"Total money raised: {totalMoneyRaised:.2f}", True, (0, 0, 0))
    maximumCapacity = font.render("Maximum capacity 30", True, (0, 0, 0))
    Totalstations = font.render("Total stations 10", True, (0, 0, 0))
    passengers = font.render(f"Passengers: {len(drawn_points)}", True, (0, 0, 0))
    MovementBus.screen.blit(moneyCollected, (460, 25))
    MovementBus.screen.blit(maximumCapacity, (460, 75))
    MovementBus.screen.blit(Totalstations, (460, 90))
    MovementBus.screen.blit(passengers, (460, 125))

def bus_positioning(x, y):
    busImg = pygame.image.load("staffBus.png")
    busInsideImg = pygame.image.load("busInside.png")
    MovementBus.screen.blit(busImg, (700, 200))
    MovementBus.screen.blit(busInsideImg, (100, 50))

def movement_strip():
    global totalMoneyRaised 
    floortextureImg = pygame.image.load("grass.png")
    stripImg = pygame.image.load("strip.jpg")
    yellowStripImg = pygame.image.load("yellow_strip.jpg")
    stopImg = pygame.image.load("stop.png")
    person = pygame.image.load("persprue.png")
    rel_y = MovementBus.numberOfYellowStripImg % 103
    if MovementBus.numberImg == 11:
        MyClass.insert_record(totalMoneyRaised)
        restart()
        from game.game_logic import Main
        Main.intro_loop()
    else:
        recreoStopImg = pygame.image.load("shutdown" + repr(MovementBus.numberImg) + ".png")
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
            if MovementBus.pauseMov < 40 and len(occupied_seats) < MAX_CAPACITY:
                MovementBus.personCont += MovementBus.movPerson
                MovementBus.screen.blit(person, (MovementBus.personCont % 150, 236))
                MovementBus.pauseMov += 1
                if MovementBus.pauseMov == 40 and len(occupied_seats) < MAX_CAPACITY:
                    for _ in range(1, random.randint(1, 12)):
                        detector.txtVideo = "person"
                        detector.face()
                        totalMoneyRaised += FARE  # pasaje
                        pygame.display.set_mode(MovementBus.size)
                        pygame.display.set_caption("Ventana")
                        draw_point(points)
                        MovementBus.positionOfOutputMovement = 135
                        MovementBus.orderMovement = False
            else:
                if len(occupied_seats) == MAX_CAPACITY:
                    probabilityOfPeopleDrop = random.randint(0, 1)
                    MovementBus.positionOfOutputMovement -= 1
                    if MovementBus.positionOfOutputMovement == 50 and MovementBus.numberImg > 1 and probabilityOfPeopleDrop == 0:
                        detector.txtVideo = "exit"
                        detector.face()
                        delete_points()
                        pygame.display.set_mode(MovementBus.size)
                        pygame.display.set_caption("Ventana")
                        MovementBus.orderMovement = True
                    if 0 < MovementBus.positionOfOutputMovement < 50 and MovementBus.orderMovement:
                        MovementBus.screen.blit(person, (MovementBus.positionOfOutputMovement % 135, 416))

        MovementBus.numberOfYellowStripImg += MovementBus.acceleration
        if MovementBus.cont <= 583:
            if MovementBus.cont % 53 == 0:
                if MovementBus.acceleration <= 11:
                    MovementBus.acceleration += 1
        else:
            if MovementBus.cont % 53 == 0 and MovementBus.cont <= 1219:
                MovementBus.acceleration -= 1

        if MovementBus.cont > 1200 and MovementBus.cont > 2000:
            if MovementBus.cont % 53 == 0:
                if MovementBus.acceleration <= 11:
                    MovementBus.acceleration += 1

        if MovementBus.cont == 2200:
            MovementBus.stopCont = 0
            MovementBus.personCont = 0
            MovementBus.stationStop = 0
            MovementBus.numberImg += 1
            MovementBus.cont = 0

def draw_point(points):
    available_seats = [point for point in points if point not in occupied_seats]
    if available_seats:
        point = random.choice(available_seats)
        drawn_points.append(point)
        occupied_seats.add(point)
        pygame.draw.circle(MovementBus.screen, red, point, 5)

def redraw_points():
    for point in drawn_points:
        pygame.draw.circle(MovementBus.screen, red, point, 5)

def delete_points():
    if drawn_points:
        point = drawn_points.pop(random.randint(0, len(drawn_points) - 1))
        occupied_seats.remove(point)

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
                if event.key == pygame.K_p:
                    paused()
        MovementBus.screen.fill((119, 119, 119))
        MovementBus.mouse = pygame.mouse.get_pos()
        fund()
        bus_positioning(0, 0)
        movement_strip()
        redraw_points()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 650 < mouse[0] < 800 and 0 < mouse[1] < 50:
            pygame.draw.rect(MovementBus.screen, silver, (650, 0, 150, 50))
            if click[0] == 1:
                paused()
        else:
            pygame.draw.rect(MovementBus.screen, white, (650, 0, 150, 50))
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("PAUSE", smallText)
        textRect.center = (725, 25)
        MovementBus.screen.blit(textSurf, textRect)
        pygame.display.flip()

framework()
