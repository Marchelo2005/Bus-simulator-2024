import sys
import pygame
from game.movement_bus import framework
from ui.main_menu import Main

def main():
    pygame.init()
    Main.intro_loop()

if __name__ == "__main__":
    main()
