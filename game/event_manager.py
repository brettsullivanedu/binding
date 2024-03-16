import pygame

class EventManager:
    """
    The EventManager handles the distribution of events to registered listeners
    within the game. It allows for a decoupled architecture where game states and
    other components can listen for and react to events without being directly linked.

    Attributes:
        listeners (list): A list of registered listeners that will receive events.
    """

    def __init__(self):
        """
        Initializes the EventManager with an empty list of listeners.
        """
        self.listeners = []

    def process_events(self, events):
        """
        Processes and distributes a batch of events to all registered listeners.
        This includes handling the pygame.QUIT event to terminate the game and
        dispatching other events to listeners for further processing.

        Parameters:
            events (list): A list of pygame events to be processed.
        """
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                self.dispatch(event)

    def register_listener(self, listener):
        """
        Registers a new listener for event notifications if it's not already registered.
        Registered listeners will receive events through their handle_event method.

        Parameters:
            listener: The listener to be registered, expected to implement a
            handle_event method.
        """
        if listener not in self.listeners:
            self.listeners.append(listener)

    def unregister_listener(self, listener):
        """
        Unregisters a listener from event notifications, removing it from the list
        of listeners if it is currently registered.

        Parameters:
            listener: The listener to be unregistered.
        """
        if listener in self.listeners:
            self.listeners.remove(listener)

    def dispatch(self, event):
        """
        Dispatches an event to all registered listeners, calling their handle_event
        method with the event as the argument.

        Parameters:
            event: The event to be dispatched.
        """
        for listener in self.listeners:
            listener.handle_event(event)
