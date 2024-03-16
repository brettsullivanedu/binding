import pygame
from game.asset_manager import AssetManager
from game.event_manager import EventManager
from game.state_manager import StateManager
from states.game_over_state import GameOver
from states.gameplay import Gameplay
from states.main_menu_state import MainMenu
from states.pause_state import Pause

class Game:
    """
    The Game class is the central component of the game application, responsible for
    initializing the game environment, managing game states, handling events, and
    executing the main game loop.

    Attributes:
        screen (pygame.Surface): The main screen surface where the game is rendered.
        clock (pygame.time.Clock): Clock used to control the game's frame rate.
        running (bool): Flag indicating if the game is running.
        font (pygame.font.Font): Default font used across different game states.
        state_manager (StateManager): Manages transitions between game states.
        asset_manager (AssetManager): Handles loading and accessing game assets.
        event_manager (EventManager): Processes and delegates events within the game.
    """

    def __init__(self):
        """
        Initializes the game, setting up the screen, clock, and managers for states,
        assets, and events. It also preloads assets and sets up initial game states.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)  # Set up a basic font

        # Initialize managers
        self.state_manager = StateManager(self)
        self.asset_manager = AssetManager()
        self.event_manager = EventManager()

        self.load_assets()  # Preload assets
        self.setup_states()  # Set up initial game states

    def load_assets(self):
        """
        Loads game assets through the AssetManager. This method can be expanded to
        load assets from a configuration file or through specific asset loading
        functions.
        """
        self.asset_manager.load_assets_from_config('assets_config.json')

    def setup_states(self):
        """
        Sets up the initial game states, adding them to the StateManager and
        setting the initial state to the MainMenu.
        """
        self.state_manager.add_state("MainMenu", MainMenu(self))
        self.state_manager.add_state("Gameplay", Gameplay(self))
        self.state_manager.add_state("Pause", Pause(self))
        self.state_manager.add_state("GameOver", GameOver(self))
        
        self.state_manager.change_state("MainMenu")

    def run(self):
        """
        Executes the main game loop, processing events, updating the current game
        state, and rendering to the screen, until the game is no longer running.
        """
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()
            
            # Handle input events for the current state.
            # This line sends all Pygame events collected at the start of the loop to the
            # current active game state for processing. This could include player movements,
            # actions, or other inputs that affect the game state.
            self.state_manager.current_state.handle_event(events)

            # Process global events that are not specific to any game state.
            # The EventManager may handle system-wide events or trigger actions that are
            # independent of the current game state, such as logging, debugging actions, or
            # global shortcuts.
            self.event_manager.process_events(events)

            # Update the current game state.
            # This call advances the game logic by one tick or frame. Depending on the current
            # state, this can involve moving game entities, handling game logic, checking for
            # collisions, or other game-specific updates.
            self.state_manager.update()

            # Render the current frame.
            self.screen.fill((0, 0, 0))  # Clear the screen with a black color before drawing the new frame.
            # This ensures that each frame starts with a blank canvas, preventing ghosting from previous frames.

            # Draw the current state's visuals to the screen.
            # Depending on the active state, this could include drawing the main menu, the game
            # playfield, pause menu, or game over screen. Each state is responsible for its own rendering.
            self.state_manager.draw(self.screen)
            
            pygame.display.flip()

            self.clock.tick(60)  # Maintain 60 frames per second

    def quit(self):
        """
        Sets the flag to exit the main game loop and clean up before quitting the game.
        """
        self.running = False
