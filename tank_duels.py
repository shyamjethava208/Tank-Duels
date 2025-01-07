import pygame
import sys
from settings import Settings
from tank import Tank
from bullet import Bullet
class Tank_duel:
    """main game class with all methods to run it"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("tank_duels")
        self.tank1 = Tank(self, "one")
        self.tank2 = Tank(self, "two")
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
        self.game_active = True
        self.clock = pygame.time.Clock()
        self.last_shot_time1 = 0
        self.last_shot_time2 = 0


    def run(self):
        """main loop of the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.tank1.update()
                self.tank2.update()
                self._update_screen()
            self.clock.tick(60)
    

    def _update_screen(self):
        # draws everything on screen
        self.display.fill(self.settings.bg_color)
        self.tank1.blitme()
        self.tank2.blitme()
        self._update_bullets()
        # holds the last drawn image on display
        pygame.display.flip()


    def _update_bullets(self):
        self._check_bullets_collision()
        self._check_tank2_collision()
        self._check_tank1_collision()
        self._draw_bullets()

    def _draw_bullets(self):
        for bullet in self.bullets1.sprites():
            bullet.update()
            bullet.blitme()
        for bullet in self.bullets2.sprites():
            bullet.update()
            bullet.blitme()

    def _check_bullets_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets1, self.bullets2,True, True)

    def _check_tank2_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets1, [self.tank2], False, False)
        if collision:
            print("tank1 won the game")
            self.game_active = False

    def _check_tank1_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets2, [self.tank1], False, False)
        if collision:
            print("tank2 won the game")
            self.game_active = False


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
        # handles key down events
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_w:
            self.tank1.moving_up = True
        if event.key == pygame.K_s:
            self.tank1.moving_down = True
        if event.key == pygame.K_UP:
            self.tank2.moving_up = True
        if event.key == pygame.K_DOWN:
            self.tank2.moving_down = True 
        if event.key == pygame.K_SPACE:
            if(self._check_can_shoot(self.last_shot_time1)):
                new_bullet = Bullet(self, "one")
                self.bullets1.add(new_bullet)
                self.last_shot_time1 = pygame.time.get_ticks()
        if event.key == pygame.K_RETURN:
            if(self._check_can_shoot(self.last_shot_time2)):
                new_bullet = Bullet(self, "two")
                self.bullets2.add(new_bullet)
                self.last_shot_time2 = pygame.time.get_ticks()
    
    def _check_can_shoot(self, player_last_shot_time):
        current_time = pygame.time.get_ticks()
        return (current_time - player_last_shot_time >= self.settings.bullet_delay)
    
    def _check_keyup_event(self, event):
        # handles key up events
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