import pygame
class Tank:
    def __init__(self, game):
        self.screen = game.display
        self.screen_rect = game.display.get_rect()
        self.original_image1 = pygame.image.load('Tank-Duel/images/tankbody.bmp')
        self.original_image2 = pygame.image.load('Tank-Duel/images/tankbody2.bmp')
        self.image1 = pygame.transform.scale(self.original_image1, (70,70))
        self.image2 = pygame.transform.scale(self.original_image2, (70,70))
        self.rect1 = self.image1.get_rect()
        self.rect1.midleft = self.screen_rect.midleft
        self.rect2 = self.image2.get_rect()
        self.rect2.midright = self.screen_rect.midright
        self.moving_up = False
        self.moving_down = False
    
    def blitme(self,playerNo):
        if playerNo == 1:
            self.screen.blit(self.image1, self.rect1)
        else:
            self.screen.blit(self.image2, self.rect2)
        # self.screen.blit(self.image1, self.rect)

    def update(self):
        if self.moving_up:
            if self.rect1.y > 0:
                self.rect1.y -= 10
        elif self.moving_down:
            if self.rect1.bottom < self.screen_rect.bottom:
                self.rect1.y += 10
        if self.moving_up:
            if self.rect2.y > 0:
                self.rect2.y -= 10
        elif self.moving_down:
            if self.rect2.bottom < self.screen_rect.bottom:
                self.rect2.y += 10