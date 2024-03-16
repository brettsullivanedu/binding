from states.game_state import GameState


class GameOver(GameState):
    def __init__(self, game):
        super().__init__(game)
        # Setup game over specifics

    def update(self):
        # Option to restart or exit
        pass

    def draw(self, screen):
        # Display game over message
        pass
