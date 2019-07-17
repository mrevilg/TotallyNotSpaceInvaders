import pygame.font

class Scoreboard():
    """A Class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.scrren_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        slef.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()