class AIBehavior:
    """
    A base class for AI behaviors. This class defines a contract for AI behaviors
    that can be assigned to enemies or other NPCs in the game. Subclasses should
    override the execute method to implement specific behavior logic.
    """
    
    def execute(self, enemy, player):
        """
        Executes the AI behavior.

        This method should be overridden by subclasses to define the specific actions
        an enemy should take when this behavior is executed, such as moving towards the
        player, avoiding obstacles, or attacking.

        Parameters:
            enemy (Enemy): The enemy entity that this behavior is controlling.
            player (Player): The player entity, often used as a target for the behavior.
        
        Raises:
            NotImplementedError: If the subclass does not override this method.
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

class ChasePlayerBehavior(AIBehavior):
    """
    A specific AI behavior where the enemy entity attempts to chase or move towards
    the player character, avoiding obstacles if necessary.
    """
    
    def execute(self, enemy, player, collision_manager):
        """
        Executes the chase player behavior. Determines the direction to move towards
        the player and adjusts the enemy's position, checking for collisions to avoid
        obstacles.

        Parameters:
            enemy (Enemy): The enemy entity executing this behavior.
            player (Player): The target player entity that the enemy is chasing.
            collision_manager (CollisionManager): The collision manager used to check
                for collisions with obstacles.
        """
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
