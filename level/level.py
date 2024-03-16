from .tile import WallTile, FloorTile

class Level:
    """Manages the game level including tiles and entities."""
    def __init__(self, game):
        self.game = game
        self.tiles = []
        self.entities = []  # Placeholder for level entities like enemies and items

    def load(self, layout):
        """Load level from a given layout."""
        self.tiles = []  # Reset/clear tiles when loading a new level
        for y, row in enumerate(layout):
            for x, col in enumerate(row):
                if col == "W":
                    self.tiles.append(WallTile(x * 50, y * 50))
                elif col == "F":
                    self.tiles.append(FloorTile(x * 50, y * 50))
                # Add more elif clauses for other tile types

    def update(self):
        """Update the level state."""
        # Here you might update entities within the level
        for entity in self.entities:
            entity.update()

    def draw(self, screen):
        """Draw the level and its entities."""
        for tile in self.tiles:
            tile.draw(screen)
        for entity in self.entities:
            entity.draw(screen)
