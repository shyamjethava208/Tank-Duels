import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.screen = game.game.display
        self.settings = game.settings
        self.original_image = pygame.image.load('Tank-Duel/images/Bullet.bmp')
        self.image = pygame.transform.scale(self.original_image, (5, 5))
        self.rect =self.image.get_rect()
        self.fire(player)
    
    def fire(self, player, game):
        if player == "one":
            self.rect.left = game.tank1.head_rect.right
    
    def blitme(self):
        self.screen.blit(self.image.self.rect)