class Settings:
    """a class to store all settings for tank_duels"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)

        self.tank_speed = 5
        self.tank_padding = 30


        self.bullet_speed = 30
        self.bullet_delay = 800