import os

import pygame

THEMES_DIR = './graphics/themes'
PREVIEW_FILES = ('wall_horizontal', 'stone_red', 'stone_yellow', 'paddle', 'ball')


class ThemeMenu:
    """Toggleable (F1) overlay to preview and select level themes."""

    def __init__(self, current):
        self.visible = False
        self.themes = sorted(d for d in os.listdir(THEMES_DIR) if os.path.isdir(os.path.join(THEMES_DIR, d)))
        self.index = self.themes.index(current) if current in self.themes else 0
        self.font = pygame.font.Font(None, 28)
        self.previews = {t: self._load_preview(t) for t in self.themes}
        self.row_rects = []

    @property
    def selected(self):
        return self.themes[self.index]

    def _load_preview(self, theme):
        images = []
        for name in PREVIEW_FILES:
            image = pygame.image.load(f'{THEMES_DIR}/{theme}/{name}.png').convert_alpha()
            if name in ('wall_horizontal', 'stone_red', 'stone_yellow'):
                image = pygame.transform.smoothscale(image, (32, 32))
            elif name == 'paddle':
                image = pygame.transform.smoothscale(image, (52, 12))
            images.append(image)
        return images

    def handle_event(self, event):
        """Returns the theme name to apply, or None."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.visible = not self.visible
            elif self.visible:
                if event.key == pygame.K_UP:
                    self.index = (self.index - 1) % len(self.themes)
                elif event.key == pygame.K_DOWN:
                    self.index = (self.index + 1) % len(self.themes)
                elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return self.selected
        elif self.visible and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, rect in enumerate(self.row_rects):
                if rect.collidepoint(event.pos):
                    self.index = i
                    return self.selected
        return None

    def draw(self):
        surface = pygame.display.get_surface()
        if not self.visible:
            hint = self.font.render('F1: Themes', True, (200, 200, 200))
            surface.blit(hint, hint.get_rect(topright=(surface.get_width() - 10, 10)))
            return

        row_h = 44
        panel = pygame.Rect(0, 0, 380, 60 + row_h * len(self.themes) + 30)
        panel.topright = (surface.get_width() - 10, 10)
        overlay = pygame.Surface(panel.size, pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 220))
        surface.blit(overlay, panel)
        pygame.draw.rect(surface, (200, 200, 200), panel, 2)

        title = self.font.render('Themes', True, 'White')
        surface.blit(title, (panel.x + 12, panel.y + 12))

        self.row_rects = []
        for i, theme in enumerate(self.themes):
            rect = pygame.Rect(panel.x + 6, panel.y + 44 + i * row_h, panel.width - 12, row_h - 4)
            self.row_rects.append(rect)
            if i == self.index:
                pygame.draw.rect(surface, (70, 90, 140), rect)
            label = self.font.render(theme, True, 'White')
            surface.blit(label, label.get_rect(midleft=(rect.x + 8, rect.centery)))
            x = rect.x + 120
            for image in self.previews[theme]:
                surface.blit(image, image.get_rect(midleft=(x, rect.centery)))
                x += image.get_width() + 4

        help_text = self.font.render('Up/Down, Enter/Click: apply', True, (180, 180, 180))
        surface.blit(help_text, (panel.x + 12, panel.bottom - 26))
