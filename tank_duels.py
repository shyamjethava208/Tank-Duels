import pygame
import sys
from settings import Settings
from tank import Tank
class Tank_duel:
    """main game class with all methods to run it"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("tank_duels")
        self.tank = Tank(self)
        self.clock = pygame.time.Clock()


    def run(self):
        """main loop of the game"""
        while True:
            self._check_events()
            self.tank.update()
            self._update_screen()
            self.clock.tick(60)
    

    def _update_screen(self):
        self.display.fill(self.settings.bg_color)
        self.tank.blitme()
        # holds the last drawn image on display
        pygame.display.flip()

    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.tank.moving_up = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.tank.moving_up = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.tank.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.tank.moving_down = False
                

if __name__ == "__main__":
    """make instance of game and run it"""
    game = Tank_duel()
    game.run()