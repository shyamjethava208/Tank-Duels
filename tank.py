import pygame
from settings import Settings
class Tank:
    def __init__(self, game, player):
        self.screen = game.display
        self.settings = Settings()
        self.screen_rect = game.display.get_rect()
        self.original_image = self.load_tank_image(player)
        self.image = pygame.transform.scale(self.original_image, (70,70))
        self.rect = self.image.get_rect()
        self.set_location(player)
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            if self.rect.y > 30:
                self.rect.y -= 10
        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom - 30:
                self.rect.y += 10
    def set_location(self, player):
        if player == "one":
            self.rect.midleft = self.screen_rect.midleft
            self.rect.x += 30
        else:
            self.rect.midright = self.screen_rect.midright
            self.rect.x = self.settings.screen_width - 100
    def load_tank_image(self, player):
        if player == "one":
            return pygame.image.load('Tank-Duel/images/tankbody.bmp')
        else:
            return pygame.image.load('Tank-Duel/images/tankbody2.bmp')