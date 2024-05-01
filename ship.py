import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #start the ship in the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        #Moving Flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """updates the ships position based off of the moving flag"""

        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
