import pygame
from states.game_state import GameState

"""
The `Pause` class extends the `GameState` class to implement the pause menu functionality within the game. This state is triggered during gameplay when the player pauses the game, providing options like resuming the game or returning to the main menu. 

Key Features and Methods:
- `__init__(self, game)`: Initializes the pause state with a reference to the main game object. It sets up the pause menu options and the currently selected menu item.
- `update(self)`: Handles the logic for navigating the pause menu options. This method should be extended to update the selection based on user input.
- `draw(self, screen)`: Renders a semi-transparent overlay on the current game screen to create a dim effect, indicating that the game is paused. It then draws the menu options, highlighting the currently selected option.
- `resume_game(self)`: A method called to resume the game, typically triggered when the "Resume" option is selected.
- `to_main_menu(self)`: Transitions the game state to the main menu, usually called when the "Main Menu" option is selected.
- `handle_event(self, events)`: Processes keyboard inputs to navigate through the pause menu options and select an option. It supports navigation with the up and down arrow keys and selection with the return or space key.

The `Pause` state is integral for providing players with the ability to temporarily halt gameplay and make selections from a set of options without leaving the game environment. It enhances the user experience by offering a seamless transition between gameplay and game management tasks.
"""

class Pause(GameState):
    """
    The Pause class represents the pause menu state of the game, providing players
    with options to either resume the game or return to the main menu. It inherits
    from GameState and overrides its methods to implement pause menu-specific logic
    and rendering.

    Attributes:
        game (Game): Reference to the main game object for accessing shared resources
            and state management.
        options (list of tuple): List of menu options as tuples, where each tuple contains
            the option text and the method to call when selected.
        selected_index (int): Index of the currently selected menu option.
    """

    def __init__(self, game):
        """
        Initializes the Pause state with the game reference, setting up the pause menu
        options and the initial selection.

        Parameters:
            game (Game): The main game object.
        """
        super().__init__(game)
        self.options = [("Resume", self.resume_game), ("Main Menu", self.to_main_menu)]
        self.selected_index = 0

    def update(self):
        """
        Updates the pause menu logic, primarily handling navigation through menu options.
        This method is called every frame and should be extended to update the selection
        based on user input.
        """
        pass

    def draw(self, screen):
        """
        Draws the pause menu to the given screen, including a semi-transparent overlay
        over the current game screen to indicate that the game is paused, and the menu
        options, highlighting the currently selected option.

        Parameters:
            screen (pygame.Surface): The screen surface to draw the pause menu on.
        """
        overlay = pygame.Surface((self.game.screen.get_width(), self.game.screen.get_height()))
        overlay.set_alpha(128)  # Semi-transparent overlay
        overlay.fill((0, 0, 0))  # Black overlay
        screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 36)
        for index, (option_text, _) in enumerate(self.options):
            color = (255, 0, 0) if index == self.selected_index else (255, 255, 255)
            text_surf = font.render(option_text, True, color)
            x = screen.get_width() / 2 - text_surf.get_width() / 2
            y = screen.get_height() / 2 + index * 40
            screen.blit(text_surf, (x, y))

    def resume_game(self):
        """
        Resumes the game by changing the current state back to Gameplay.
        """
        self.game.state_manager.change_state("Gameplay")

    def to_main_menu(self):
        """
        Returns to the main menu by changing the current state to MainMenu.
        """
        self.game.state_manager.change_state("MainMenu")

    def handle_event(self, events):
        """
        Handles input events for navigating the pause menu options or selecting an option.
        Updates the selected option based on user input and executes the selected option's
        action when enter or space is pressed.

        Parameters:
            events (list): A list of events to be processed.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    _, action = self.options[self.selected_index]
                    action()