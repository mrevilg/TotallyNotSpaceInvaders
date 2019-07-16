class GameStats():
    """Track statistics for Totally Not Space Invaders."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that happen during the game."""
        self.ship_left = self.ai_settings.ship_limit