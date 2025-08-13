import pygame, math


class Calculator:
    def __init__(self):
        self.__width = 700
        self.__height = 1200

    def drawButtons(self):
        button0 = pygame.draw.rect()


    def showScreen(self):
        pygame.display.set_caption("Calculator")
        pygame.display.set_mode((self.__width, self.__height))
        run = True
        while run:
            event = pygame.event.get()
            for event in event:
                if event.type == pygame.QUIT:
                    run = False


            pygame.display.update()



instance = Calculator()
instance.showScreen()
