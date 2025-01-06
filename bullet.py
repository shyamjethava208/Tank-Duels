import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game, player):
        super().__init__()
        self.screen = game.display
        self.settings = game.settings
        self.original_image = pygame.image.load('Tank-Duel/images/Bullet.bmp')
        self.image = pygame.transform.scale(self.original_image, (30, 5))
        self.rect = self.image.get_rect()
        self.fire(player, game)
        self.player = player
    
    def fire(self, player, game):
        if player == "one":
            print("called fire")
            print(game.tank1.head_rect.right)
            self.rect.midleft = game.tank1.head_rect.midright
            self.rect.x -= 30
            print(self.rect.left)
        else:
            self.rect.midright = game.tank2.head_rect.midleft

    def update(self):
        if self.player == "one":
            self.rect.x += 10
        else:
            self.rect.x -= 10

    def blitme(self):
        self.screen.blit(self.image,self.rect)