from .entity import Entity

class Enemy(Entity):
    def __init__(self, x, y, sprite, health, ai_behavior=None):
        super().__init__(x, y, sprite, health)
        self.ai_behavior = ai_behavior
        self.speed = 1

    def update(self, player, collision_manager):
        if self.ai_behavior:
            self.ai_behavior.execute(self, player, collision_manager)
            
    def die(self):
        print("Player has died.")
        # Transition to a game over state could be handled here

