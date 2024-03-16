# state_manager.py
"""
The `StateManager` class is a central component of the game's architecture, designed to manage the transitions between different game states (e.g., MainMenu, Gameplay, Pause) and delegate the flow of control to the active state. It acts as a switchboard, ensuring that the game can smoothly transition from one state to another, thereby encapsulating the logic for state management away from the main game loop.

Key Functionalities:
- `__init__(self, game)`: Initializes the StateManager with a reference to the main game object, allowing states to access shared resources and other game-related functionality. It also prepares a container for storing the different states and tracks the currently active state.
- `add_state(self, name, state)`: Registers a new state with the StateManager under a given name. This method allows for the dynamic addition of states, making the system flexible and extensible.
- `change_state(self, name)`: Handles the transition from the current state to a new state identified by `name`. It ensures that exit procedures for the outgoing state are run (such as resource cleanup), and enter procedures for the incoming state are initiated (such as setting up the state's environment).
- `update(self)`: Delegates the update logic to the currently active state, allowing each state to independently manage its internal logic, such as handling user inputs, updating game entities, and performing collision detection.
- `draw(self, screen)`: Invokes the draw method of the current state, enabling each state to control how it is rendered on the screen. This method supports the separation of game logic from rendering logic, adhering to good software design practices.
- `handle_event(self, event)`: Forwards event handling to the currently active state, ensuring that only the active state responds to user inputs and other events. This centralized event management simplifies the handling of state-specific actions and interactions.

The `StateManager` ensures a cohesive yet decoupled relationship between the game's overarching control flow and the individual states, allowing each state to focus on its specific responsibilities while the `StateManager` handles the transitions and delegation of control. This design promotes modularity, scalability, and maintainability within the game's architecture.
"""

class StateManager:
    def __init__(self, game):
        """
        Initialize the StateManager with a reference to the main game object.
        
        This manager is responsible for storing all possible states the game can be in,
        managing transitions between these states, and delegating calls to update,
        draw, and handle events to the current state.
        
        Parameters:
            game: A reference to the main game object which holds the state manager.
        """
        self.game = game
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        """
        Add a new state to the manager.
        
        Parameters:
            name (str): The name of the state to add.
            state (object): The state object to add under the given name.
        """
        self.states[name] = state

    def change_state(self, name):
        """
        Change the current state to a different state identified by `name`.
        
        Before changing, it calls the exit method of the current state (if any),
        and after changing, it calls the enter method of the new state. If the specified
        state does not exist, it logs a warning and does not change the state.
        
        Parameters:
            name (str): The name of the state to switch to.
        """
        if name not in self.states:
            print(f"Warning: The state '{name}' does not exist.")
            return

        if self.current_state:
            self.current_state.exit()

        self.current_state = self.states[name]
        if self.current_state:
            self.current_state.enter()

    def update(self):
        """
        Update the current state.
        
        Delegates the update method call to the currently active state, if any.
        This allows the active state to handle its internal logic independently.
        """
        if self.current_state:
            self.current_state.update()

    def draw(self, screen):
        """
        Draw the current state to the given screen.
        
        Delegates the draw method call to the currently active state, allowing
        each state to control its own rendering process.
        
        Parameters:
            screen: The screen or surface to draw the current state on.
        """
        if self.current_state:
            self.current_state.draw(screen)

    def handle_event(self, event):
        """
        Pass an event to the current state for processing.
        
        Delegates the event handling to the currently active state, ensuring
        that only the active state responds to user inputs and other events.
        
        Parameters:
            event: The event to be handled by the current state.
        """
        if self.current_state:
            self.current_state.handle_event(event)
