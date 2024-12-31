import pygame
import sys
from settings import Settings
class Tank_duel:
    """main game class with all methods to run it"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("tank_duels")
        self.clock = pygame.time.Clock()


    def run(self):
        """main loop of the game"""
        while True:
            self._check_events()
            # holds the last drawn image on display
            self.display.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)
    
    def _check_events(self):
        # watch for keyboard and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == "__main__":
    """make instance of game and run it"""
    game = Tank_duel()
    game.run()