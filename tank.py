import pygame
class Tank:
    """A class to manage tank"""
    def __init__(self, game, player):
        self.game = game
        self.screen = game.display
        self.settings = game.settings
        self.player = player
        self.screen_rect = game.display.get_rect()
        self.original_image = self.load_tank_image()
        self.image = pygame.transform.scale(self.original_image, (70,70))
        self.rect = self.image.get_rect()
        self.set_location()
        self.head_original_image = self.load_tank_head_image()
        self.head_image = pygame.transform.scale(self.head_original_image, (70,70))
        self.head_rect = self.head_image.get_rect()
        self.head_rect.center = self.rect.center    
        self.moving_up = False
        self.moving_down = False
        self.life = 3

    
    def blitme(self):
        # draw tank on screen
        self.screen.blit(self.image, self.rect)
        if self.game.game_active:
            self.screen.blit(self.head_image, self.head_rect)

    def update(self):
        if self.moving_up:
            if self.rect.y > self.settings.tank_padding:
                self.rect.y -= self.settings.tank_speed
        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom - self.settings.tank_padding:
                self.rect.y += self.settings.tank_speed
        self.head_rect.center = self.rect.center

    def set_location(self):
        # sets the tank position initially 
        if self.player == "one":
            self.rect.midleft = self.screen_rect.midleft
            self.rect.x += self.settings.tank_padding
        else:
            self.rect.midright = self.screen_rect.midright
            self.rect.x -= self.settings.tank_padding

    def load_tank_head_image(self):
        if self.player == "one":
            return pygame.image.load('images/tankhead.bmp')
        else:
            return pygame.image.load('images/tankhead2.bmp')
    
    def load_tank_image(self):
        if self.player == "one":
            return pygame.image.load('images/tankbody.bmp')
        else:
            return pygame.image.load('images/tankbody2.bmp')
