# ai_manager.py
class AIBehavior:
    def execute(self, enemy, player):
        raise NotImplementedError("This method should be overridden by subclasses.")

class ChasePlayerBehavior(AIBehavior):
    def execute(self, enemy, player, collision_manager):
        # Determine the direction of movement towards the player
        dx = enemy.speed if player.x > enemy.x else -enemy.speed if player.x < enemy.x else 0
        dy = enemy.speed if player.y > enemy.y else -enemy.speed if player.y < enemy.y else 0

        # Create hypothetical rects for testing collision after moving
        test_rect_x = enemy.rect.copy()
        test_rect_x.x += dx
        test_rect_y = enemy.rect.copy()
        test_rect_y.y += dy
        
        # Check for wall collisions before moving horizontally
        if not collision_manager.check_tile_collision(test_rect_x, "Wall"):
            enemy.rect.x += dx
            enemy.x = enemy.rect.x  # Update the enemy's x-coordinate
        
        # Check for wall collisions before moving vertically
        if not collision_manager.check_tile_collision(test_rect_y, "Wall"):
            enemy.rect.y += dy
            enemy.y = enemy.rect.y  # Update the enemy's y-coordinate

# Further behaviors can be defined following the AIBehavior contract.
