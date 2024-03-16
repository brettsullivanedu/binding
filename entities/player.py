import pygame
from .entity import Entity

class Player(Entity):
    def __init__(self, x, y, sprite, health):
        super().__init__(x, y, sprite, health)
        self.speed = 5
        self.direction = pygame.math.Vector2(0, 0)  # Movement direction
        # Initialize movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def move(self, dx, dy):
        # Before moving, you could check for collisions or tile restrictions here
        # For simplicity, we'll just update the position directly
        super().move(dx, dy)  # Call the move method from the Entity base class


    def update(self, collision_manager):
        # Calculate the desired movement
        dx = (self.moving_right - self.moving_left) * self.speed
        dy = (self.moving_down - self.moving_up) * self.speed

        # Create a copy of rect for hypothetical movement
        new_rect = self.rect.copy()
        new_rect.x += dx
        new_rect.y += dy
        
        # Check for wall collisions. Only move if there's no collision
        if not collision_manager.check_tile_collision(new_rect, "Wall"):
            self.rect = new_rect
            self.x = self.rect.x
            self.y = self.rect.y

    def handle_event(self, event):
        # Respond to key press and release events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # Assuming WASD for movement
                self.moving_left = True
            elif event.key == pygame.K_d:
                self.moving_right = True
            elif event.key == pygame.K_w:
                self.moving_up = True
            elif event.key == pygame.K_s:
                self.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.moving_left = False
            elif event.key == pygame.K_d:
                self.moving_right = False
            elif event.key == pygame.K_w:
                self.moving_up = False
            elif event.key == pygame.K_s:
                self.moving_down = False
    

    def attack(self):
        # Placeholder for attack method
        pass

    def die(self):
        super().die()  # Call the die method from the Entity base class
        print("Player has died.")