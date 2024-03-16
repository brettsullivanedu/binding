# collision_manager.py
class CollisionManager:
    def __init__(self, level):
        self.level = level  # The level containing tile information

    def check_entity_collision(self, entity1, entity2):
        # Simple AABB collision detection
        return entity1.rect.colliderect(entity2.rect)

    def check_tile_collision(self, test_rect, tile_type):
        for tile in self.level.tiles:
            if tile.tile_type == tile_type and test_rect.colliderect(tile.rect):
                return True
        return False

