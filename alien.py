import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent an alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize alien and starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load and set alien rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien at the top lefgt of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the aliens exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the alien at it current location."""
        self.screen.blit(self.image, self.rect)