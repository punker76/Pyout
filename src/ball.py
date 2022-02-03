import pygame
import random

from settings import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, movable_sprites):
        super().__init__()
        for g in groups:
            g.add(self)

        self.image = pygame.image.load('./graphics/test/ballBlue.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pygame.Rect(pos, (TILESIZE, TILESIZE)).center
        self.rect.size = self.image.get_size()
        self.hitbox = self.rect

        self.direction = pygame.math.Vector2(-1, -1)
        self.speed = random.randrange(4, 8)

        self.obstacle_sprites = obstacle_sprites
        self.movable_sprites = movable_sprites

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision(self.obstacle_sprites, 'horizontal')
        self.collision(self.movable_sprites, 'horizontal')

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.y += self.direction.y * speed
        self.collision(self.obstacle_sprites, 'vertical')
        self.collision(self.movable_sprites, 'vertical')

        self.rect.center = self.hitbox.center

    def collision(self, sprites, direction):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        if direction == 'horizontal':
            for sprite in sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.direction.x = -1
                        self.hitbox.right = sprite.hitbox.left
                    elif self.direction.x < 0:  # moving left
                        self.direction.x = 1
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.direction.y = -1
                        self.hitbox.bottom = sprite.hitbox.top
                    elif self.direction.y < 0:  # moving up
                        self.direction.y = 1
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.move(self.speed)
