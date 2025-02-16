class Settings():
    def __init__(self):
        self.screen_width = 1030
        self.screen_height = 650
        self.bg_color = (230,230,230)

        self.ship_limit = 3

        #Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 4
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        self.speedup_factor = 1.1
        self.score_scale = 1.5

        #Alien settings
        self.fleet_drop_speed = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = .5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_factor
        self.bullet_speed_factor *= self.speedup_factor
        self.alien_speed_factor *= self.speedup_factor
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)