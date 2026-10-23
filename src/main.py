# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pygame

from settings import *
from level import Level
from menu import Menu, NEW_GAME, EXIT


class Game:
    def __init__(self):
        print("Pyout started")
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Pyout')
        self.clock = pygame.time.Clock()

        self.menu = Menu()
        self.level = None  # created when a new game starts

    def quit(self):
        print("Pyout terminated")
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if self.level is None:
                    action = self.menu.handle_event(event)
                    if action == NEW_GAME:
                        self.level = Level()
                    elif action == EXIT:
                        self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # back to the start screen
                    self.level = None

            # clear screen
            self.screen.fill((25, 25, 25))

            if self.level is None:
                self.menu.draw()
            else:
                self.level.run()

            # update screen
            # pygame.display.update() # allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
            pygame.display.flip()  # will update the contents of the entire display

            # refresh time
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
