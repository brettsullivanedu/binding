class Entity:
    def __init__(self, x, y, sprite, health):
        self.x = x
        self.y = y
        self.sprite = sprite  # This would be a pygame.Surface object
        self.health = health
        # Initialize the rect attribute based on the sprite size
        self.rect = sprite.get_rect(topleft=(x, y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        # Update the rect position as well
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.die()

    def die(self):
        pass  # Placeholder for death behavior
