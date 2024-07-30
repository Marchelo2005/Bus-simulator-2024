import pygame

class Buttons:
    def createButton(screen, x, y, width, height, text):
        pygame.font.init()
        font = pygame.font.Font("freesansbold.ttf", 20)
        text_surface, text_rect = Buttons.textObjects(text, font)
        text_rect.center = ((x + (width / 2)), (y + (height / 2)))
        screen.blit(text_surface, text_rect)

    @staticmethod
    def textObjects(text, font):
        color = (0, 0, 0)
        text_surface = font.render(text, True,color)
        return text_surface, text_surface.get_rect()
    @staticmethod
    def buttonDrawing(screen,white,x,y,width,height,):
        pygame.draw.rect(screen, white, (x, y, width, height))
