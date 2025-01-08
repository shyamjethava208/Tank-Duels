import pygame
class Wall:
    """A class that manages walls"""
    def __init__(self, game):
        self.screen = game.display
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.original_image = pygame.image.load('images/wall.bmp')
        self.image = pygame.transform.scale(self.original_image,(20,50))
        self.rect = self.image.get_rect()
        self.rect.x += 250
        self.rect.y += 250
    def blitme(self):
        # draw wall
        self.screen.blit(self.image, self.rect)