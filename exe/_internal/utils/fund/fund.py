import pygame
from utils.variables.variable.variable import variable
from utils.constants.constantWindow.constantWindow import window

def fund():
    variable.passengerCounter=variable.totalMoneyRaised/0.35
    font=pygame.font.SysFont(None,20)  
    moneyCollected = font.render(f"Total money raised : {variable.totalMoneyRaised:.2f}", True, (0, 0, 0))
    maximumCapacity = font.render("Maximum capacity 30", True, (0, 0, 0))
    Totalstations = font.render(f"station :{variable.numberImg:.0f}", True, (0, 0, 0))
    passengers = font.render(f"Total Passengers : {variable.passengerCounter:.0f}", True, (0, 0, 0))
    window.screen.blit(moneyCollected, (460, 25))
    window.screen.blit(maximumCapacity, (460, 75))
    window.screen.blit(Totalstations, (460, 90))
    window.screen.blit(passengers, (460, 125))
