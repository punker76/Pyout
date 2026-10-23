import pygame

from settings import *

NEW_GAME = 'new_game'
EXIT = 'exit'


class Menu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.title_font = pygame.font.Font(None, 120)
        self.item_font = pygame.font.Font(None, 60)
        self.hint_font = pygame.font.Font(None, 28)
        self.items = [('New Game', NEW_GAME), ('Exit', EXIT)]
        self.selected = 0

    def handle_event(self, event):
        """Returns NEW_GAME or EXIT when an entry is chosen, otherwise None."""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.items)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.items)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
                return self.items[self.selected][1]
            elif event.key == pygame.K_ESCAPE:
                return EXIT
        elif event.type == pygame.MOUSEMOTION:
            for i, rect in enumerate(self._item_rects()):
                if rect.collidepoint(event.pos):
                    self.selected = i
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self._item_rects()):
                if rect.collidepoint(event.pos):
                    return self.items[i][1]
        return None

    def _item_rects(self):
        rects = []
        for i, (label, _) in enumerate(self.items):
            surf = self.item_font.render(label, True, 'White')
            rects.append(surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 80)))
        return rects

    def draw(self):
        title = self.title_font.render('PYOUT', True, (220, 60, 60))
        self.display_surface.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 4)))

        for i, ((label, _), rect) in enumerate(zip(self.items, self._item_rects())):
            color = (255, 220, 60) if i == self.selected else (180, 180, 180)
            self.display_surface.blit(self.item_font.render(label, True, color), rect)

        hint = self.hint_font.render('Up/Down: select   Enter: confirm   Esc: back', True, (120, 120, 120))
        self.display_surface.blit(hint, hint.get_rect(center=(WIDTH // 2, HEIGHT - 40)))
