import pygame
class Tank:
    def __init__(self, game):
        self.screen = game.display
        self.screen_rect = game.display.get_rect()
        self.original_image = pygame.image.load('images/tankbody.bmp')
        self.image = pygame.transform.scale(self.original_image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            if self.rect.y > 0:
                self.rect.y -= 10
        elif self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.rect.y += 10