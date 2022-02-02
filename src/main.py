# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pygame

from settings import *
from level import Level


class Game:
    def __init__(self):
        print("Pyout started")
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pyout')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    print("Pyout terminated")
                    pygame.quit()
                    sys.exit()

            # clear screen
            self.screen.fill('black')

            self.level.run()

            # update screen
            # pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
            pygame.display.flip()  # will update the contents of the entire display

            # refresh time
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
