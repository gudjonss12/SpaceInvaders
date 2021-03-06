import pygame


class Settings():
    """ A class to store all settings for Monsters are coming."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 170, 1, 20
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase_speed
        self.score_scale = 1.5

        # Assign sounds to variables
        self.player_shot = pygame.mixer.Sound('./audio/laser.wav')
        self.explosion = pygame.mixer.Sound('./audio/explosion.wav')

        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        """Initalize settings that change throughout the game."""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.7
        self.alien_speed_factor = 0.2

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien score values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
