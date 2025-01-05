import pygame
import sys
from settings import Settings
from tank import Tank
class Tank_duel:
    """main game class with all methods to run it"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("tank_duels")
        self.tank1 = Tank(self, "one")
        self.tank2 = Tank(self, "two")
        self.clock = pygame.time.Clock()


    def run(self):
        """main loop of the game"""
        while True:
            self._check_events()
            self.tank1.update()
            self.tank2.update()
            self._update_screen()
            self.clock.tick(60)
    

    def _update_screen(self):
        self.display.fill(self.settings.bg_color)
        self.tank1.blitme()
        self.tank2.blitme()
        # holds the last drawn image on display
        pygame.display.flip()

    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_event(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_w:
            self.tank1.moving_up = True
        if event.key == pygame.K_s:
            self.tank1.moving_down = True
        if event.key == pygame.K_UP:
            self.tank2.moving_up = True
        if event.key == pygame.K_DOWN:
            self.tank2.moving_down = True 
    
    def _check_keyup_event(self, event):
        if event.key == pygame.K_w:
            self.tank1.moving_up = False
        if event.key == pygame.K_s:
            self.tank1.moving_down = False
        if event.key == pygame.K_UP:
            self.tank2.moving_up = False
        if event.key == pygame.K_DOWN:
            self.tank2.moving_down = False

if __name__ == "__main__":
    """make instance of game and run it"""
    game = Tank_duel()
    game.run()