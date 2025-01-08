import pygame
import sys
from settings import Settings
from tank import Tank
from bullet import Bullet
from wall import Wall
from button import Button
class Tank_duel:
    """main game class with all methods to run it"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.display = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("tank_duels")
        self.game_active = True
        self.tank1 = Tank(self, "one")
        self.tank2 = Tank(self, "two")
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.last_shot_time1 = 0
        self.last_shot_time2 = 0
        self.wall = Wall(self)
        self.play_button = Button(self, "Play")

    def run(self):
        """main loop of the game"""
        while True:
            # self.play_button.draw_button()
            # pygame.display.flip()
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
        # self.wall.blitme()
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
        pygame.sprite.groupcollide(self.bullets1, self.bullets2,True, True)

    def _check_tank2_collision(self):
        # fix this later
        collision = pygame.sprite.groupcollide(self.bullets1, [self.tank2], True, False)
        if collision:
            # print(collision)
            if self.tank2.life == 1:
                print(self.tank2.life)
                print("tank1 won the game")
                self.game_active = False
                self.tank2.blitme()
                self.tank2.life -= 1
            else:
                self.tank2.life -= 1

    def _check_tank1_collision(self):
        # fix this later
        collision = pygame.sprite.groupcollide(self.bullets2, [self.tank1], True, False)
        if collision:
            # print(collision)
            if self.tank1.life == 1:
                print(self.tank1.life)
                print("tank2 won the game")
                self.game_active = False
                self.tank1.blitme()
                self.tank1.life -= 1
            else:
                self.tank1.life -= 1


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
            # refactor it later
            if(self._check_can_shoot(self.last_shot_time1)):
                new_bullet = Bullet(self, "one")
                self.bullets1.add(new_bullet)
                self.last_shot_time1 = pygame.time.get_ticks()
        if event.key == pygame.K_RETURN:
            # refactor it later
            if(self._check_can_shoot(self.last_shot_time2)):
                new_bullet = Bullet(self, "two")
                self.bullets2.add(new_bullet)
                self.last_shot_time2 = pygame.time.get_ticks()
        if event.key == pygame.K_0:
            # refactor it later
            self.tank1.set_location()
            self.tank2.set_location()
            self.tank1.life = 3
            self.tank2.life = 3
            self.bullets1.empty()
            self.bullets2.empty()
            self.game_active = True

    
    def _check_can_shoot(self, player_last_shot_time):
        current_time = pygame.time.get_ticks()
        return (current_time - player_last_shot_time >= self.settings.bullet_delay)
    
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