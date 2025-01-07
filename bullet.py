import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.screen = game.display
        self.settings = game.settings
        self.player = player
        self.original_image = self.load_image()
        self.image = pygame.transform.scale(self.original_image, (30, 5))
        self.rect = self.image.get_rect()
        self.fire(game)
    
    def load_image(self):
        if self.player == "one":
            return pygame.image.load('images/Bullet.bmp')
        else:
            return pygame.image.load('images/Bullet2.bmp')

    def fire(self, game):
        if self.player == "one":
            self.rect.midleft = game.tank1.head_rect.midright
        else:
            self.rect.midright = game.tank2.head_rect.midleft

    def update(self):
        if self.player == "one":
            self.rect.x += self.settings.bullet_speed
        else:
            self.rect.x -= self.settings.bullet_speed

    def blitme(self):
        self.screen.blit(self.image,self.rect)