class GameStats:
    """Track statistics for alien Invasion."""
    def __init__(self, ai_game):
        """Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start ga,e in inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0


    def reset_stats(self):
        """Initialize ststistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
