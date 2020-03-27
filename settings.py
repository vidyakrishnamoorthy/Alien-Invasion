class Settings():
    def __init__(self):
        self.screen_width = 1030
        self.screen_height = 600
        self.bg_color = (230,230,230)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 4
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed_factor = .5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1