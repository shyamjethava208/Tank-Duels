import pygame
from settings import Settings
class Tank:
    """A class to manage tank"""
    def __init__(self, game, player):
        self.screen = game.display
        self.settings = Settings()
        self.screen_rect = game.display.get_rect()
        self.original_image = self.load_tank_image(player)
        self.image = pygame.transform.scale(self.original_image, (70,70))
        self.rect = self.image.get_rect()
        self.set_location(player)
        self.head_original_image = self.load_tank_head_image(player)
        self.head_image = pygame.transform.scale(self.head_original_image, (70,70))
        self.head_rect = self.head_image.get_rect()
        self.head_rect.center = self.rect.center    
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        # draw tank on screen
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.head_image, self.head_rect)

    def update(self):
        # updates the movements of the tank
        if self.moving_up:
            if self.rect.y > 30:
                self.rect.y -= 10
        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom - 30:
                self.rect.y += 10
        self.head_rect.center = self.rect.center

    def set_location(self, player):
        # sets the tank position initially 
        if player == "one":
            self.rect.midleft = self.screen_rect.midleft
            self.rect.x += 30
        else:
            self.rect.midright = self.screen_rect.midright
            self.rect.x = self.settings.screen_width - 100

    def load_tank_head_image(self, player):
        if player == "one":
            return pygame.image.load('Tank-Duel/images/tankhead.bmp')
        else:
            return pygame.image.load('Tank-Duel/images/tankhead2.bmp')
    
    def load_tank_image(self, player):
        if player == "one":
            return pygame.image.load('Tank-Duel/images/tankbody.bmp')
        else:
            return pygame.image.load('Tank-Duel/images/tankbody2.bmp')