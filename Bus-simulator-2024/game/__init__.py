import sys
import os
import pygame
from game.game_logic import movementStrip, restart, drawPoint, redrawPoints
from ui.ui_elements import paused, fund, busPositioning, handle_pause_button

def main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ventana")
    clock = pygame.time.Clock()
    totalMoneyRaised = 0
    drawn_points = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused(screen)
        
        screen.fill((119, 119, 119))
        fund(screen, totalMoneyRaised)
        busPositioning(screen)
        movementStrip(screen, totalMoneyRaised, drawn_points)
        redrawPoints(screen, drawn_points)
        
        handle_pause_button(screen)
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

