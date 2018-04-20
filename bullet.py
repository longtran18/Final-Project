import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    # class to manage bullets
    def __init__(self, ai_settings, screen, ship):
        # create bullet object
        super().__init__()
        self.screen = screen

        # create a bullet
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # store bullet pos as decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        # move bullet up screen
        # update decimal pos of the bullet
        self.y -= self.speed_factor
        # update rect pos
        self.rect.y = self.y
        # print("bullet update is calling")
    
    def draw_bullet(self):
        # draw bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        # print("draw bullet is calling")
        