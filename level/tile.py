import pygame

class Tile:
    """Base class for all tiles."""
    def __init__(self, x, y, width, height, color, tile_type):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.tile_type = tile_type  # New attribute to identify the tile type

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class WallTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, (100, 100, 100), 'Wall')

class FloorTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50, (200, 200, 200), 'Floor')

