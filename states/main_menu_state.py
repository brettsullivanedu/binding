import pygame

class MainMenu:
    """
    The MainMenu class represents the main menu state of the game, providing players
    with options like starting a new game or exiting. It handles the rendering of menu
    options, navigation between options, and executing the selected option's action.

    Attributes:
        game (Game): Reference to the main game object, used to access global functionalities
            and state management.
        options (list): List of menu options as strings.
        selected_option (int): Index of the currently selected menu option.
        font (pygame.font.Font): Font used for rendering menu option texts.
    """

    def __init__(self, game):
        """
        Initializes the MainMenu with the game reference, setting up the menu options,
        the initial selection, and the font for text rendering.

        Parameters:
            game (Game): The main game object.
        """
        self.game = game
        self.options = ["Start Game", "Exit"]
        self.selected_option = 0
        self.font = pygame.font.Font(None, 36)  # Default font and size

    def enter(self):
        """
        Called when the MainMenu state is entered. It registers the MainMenu as an event
        listener to the game's event manager to receive input events.
        """
        self.game.event_manager.register_listener(self)

    def exit(self):
        """
        Called when exiting the MainMenu state. It unregisters the MainMenu from the game's
        event manager, stopping it from receiving further input events.
        """
        self.game.event_manager.unregister_listener(self)

    def update(self):
        """
        Updates the MainMenu logic. This method is called every frame and is reserved for
        future logic that doesn't involve event handling, such as animations.
        """
        pass

    def draw(self, screen):
        """
        Draws the MainMenu options to the given screen. Highlights the currently selected
        option to provide visual feedback to the player.

        Parameters:
            screen (pygame.Surface): The screen surface to draw the menu options on.
        """
        screen.fill((0, 0, 0))  # Clear screen with black background
        for i, option in enumerate(self.options):
            color = (255, 0, 0) if i == self.selected_option else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, 150 + i*40))

    def handle_event(self, events):
        """
        Handles input events for navigating the menu options or selecting an option. Updates
        the selected option based on user input (up/down arrows) and executes the selected
        option's action when enter is pressed.

        Parameters:
            events (list): A list of events to be processed.
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_option = max(0, self.selected_option - 1)
                elif event.key == pygame.K_DOWN:
                    self.selected_option = min(len(self.options) - 1, self.selected_option + 1)
                elif event.key == pygame.K_RETURN:
                    if self.selected_option == 0:  # Start Game
                        self.game.state_manager.change_state("Gameplay")
                    elif self.selected_option == 1:  # Exit
                        pygame.quit()
                        exit()