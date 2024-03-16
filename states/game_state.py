"""
This module defines the `GameState` class, serving as a template for individual game states within the game's lifecycle. A game state represents a distinct phase or mode of the game, such as the main menu, gameplay, pause menu, or game over screen. The `GameState` class is designed to encapsulate all the functionality relevant to a specific state, including initialization of resources, handling user input, updating game logic, and rendering visuals to the screen.

The class provides a set of methods that can be overridden by subclasses to implement the behavior specific to each state:

- `__init__(self, game)`: Constructor that initializes the game state with a reference to the main game object, allowing access to shared resources and other states.
- `enter(self)`: Called when transitioning into the state, used for setting up resources and initializing any state-specific elements or variables.
- `exit(self)`: Called when exiting the state, for cleaning up resources and performing any necessary state-specific shutdown procedures.
- `update(self)`: Used for updating the state's logic, such as processing game events, updating the positions of game entities, and handling transitions between states.
- `draw(self, screen)`: Renders the state's elements to the screen. This method takes a screen (or surface) object as a parameter, onto which the state's visual components are drawn.
- `handle_event(self, event)`: Processes events specific to the state, such as keyboard and mouse input. This method allows each state to respond differently to user actions.

By deriving from `GameState`, different states of the game can be implemented with their unique behavior while maintaining a consistent interface for the game's main loop to interact with.
"""

class GameState:
    def __init__(self, game):
        """
        Initialize a new game state.
        
        This constructor should be called by subclasses to ensure that each state
        has access to the main game object, which facilitates interaction with
        the game's resources, other states, and the state manager.
        
        Parameters:
            game: A reference to the main game object, providing access to shared
            resources, the state manager, and other utilities.
        """
        self.game = game

    def enter(self):
        """
        Called when a state is entered and becomes the active state.
        
        This method should be overridden by subclasses to perform any setup required
        when transitioning into the state, such as initializing resources, resetting
        variables, or preparing the game environment for this state.
        """
        pass

    def exit(self):
        """
        Called when exiting the current state.
        
        This method should be overridden by subclasses to clean up resources specific
        to the state, such as deallocating memory, saving state progress, or other
        cleanup tasks before transitioning out of the state.
        """
        pass

    def update(self):
        """
        Update the state's logic.
        
        This method should be overridden by subclasses to implement the state-specific
        logic that needs to be processed each frame, such as handling game events,
        updating game entity positions, and managing transitions between states.
        """
        pass

    def draw(self, screen):
        """
        Draw the state's visual elements to the screen.
        
        This method should be overridden by subclasses to render the state's visual
        components. The method takes a screen (or surface) object as a parameter,
        onto which the state's visuals are drawn.
        
        Parameters:
            screen: The Pygame screen (or surface) to draw the visuals on.
        """
        pass

    def handle_event(self, event):
        """
        Handle input events specific to the state.
        
        This method should be overridden by subclasses to process input events, such
        as keyboard presses and mouse clicks, that are specific to the state. It allows
        each state to respond uniquely to user inputs.
        
        Parameters:
            event: The event to process, typically passed from the Pygame event queue.
        """
        pass
