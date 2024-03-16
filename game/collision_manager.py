class CollisionManager:
    """
    The CollisionManager is responsible for managing collision detection in the game.
    It offers methods to check for collisions between entities (e.g., characters, enemies)
    and between entities and the environment (specific tile types within the level).

    Attributes:
        level (Level): The level object containing tile information necessary for
            collision checks against the environment.
    """

    def __init__(self, level):
        """
        Initializes the CollisionManager with a reference to the level object.

        Parameters:
            level (Level): The level containing tile information for environment collision checks.
        """
        self.level = level

    def check_entity_collision(self, entity1, entity2):
        """
        Checks for collisions between two entities using Axis-Aligned Bounding Box (AABB) collision detection.

        Parameters:
            entity1: The first entity involved in the collision check.
            entity2: The second entity involved in the collision check.

        Returns:
            bool: True if the entities collide, False otherwise.
        """
        return entity1.rect.colliderect(entity2.rect)

    def check_tile_collision(self, test_rect, tile_type):
        """
        Checks for collisions between a given rectangle (representing an entity's bounding box)
        and tiles of a specific type within the level.

        Parameters:
            test_rect (pygame.Rect): The rectangle to test for collisions.
            tile_type (str): The type of tile to check for collisions with.

        Returns:
            bool: True if there is a collision with the specified tile type, False otherwise.
        """
        for tile in self.level.tiles:
            if tile.tile_type == tile_type and test_rect.colliderect(tile.rect):
                return True
        return False
