# event_manager.py
import pygame

class EventManager:
    def __init__(self):
        self.listeners = []

    def process_events(self, events):
        """Fetch and distribute events to all registered listeners."""
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                self.dispatch(event)

    def register_listener(self, listener):
        """Register a new listener for event notifications."""
        if listener not in self.listeners:
            self.listeners.append(listener)

    def unregister_listener(self, listener):
        """Unregister a listener from event notifications."""
        if listener in self.listeners:
            self.listeners.remove(listener)

    def dispatch(self, event):
        """Dispatch an event to all registered listeners."""
        for listener in self.listeners:
            listener.handle_event(event)
