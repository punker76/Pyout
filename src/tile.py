import pygame

from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, filename, groups):
        super().__init__()
        for g in groups:
            g.add(self)

        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect
