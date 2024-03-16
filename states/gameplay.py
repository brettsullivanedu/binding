import pygame
from game.ai_manager import ChasePlayerBehavior
from game.collision_manager import CollisionManager
from level.level import Level
from entities.enemy import Enemy
from entities.player import Player
from states.game_state import GameState

"""
The `Gameplay` class is a concrete implementation of `GameState` that manages the main gameplay logic of the game. This state is where the core game actions, interactions, and mechanics occur, including player movement, enemy behavior, collision detection, and level progression.

Key Components and Behaviors:
- `__init__(self, game)`: Initializes the gameplay state with necessary game entities such as the player, enemies, and the level. It loads necessary assets and sets up the game environment based on the game's current state or level configuration.
- `enter(self)`: Prepares the game state for entering the main gameplay, including setting up or resetting the level, player, and enemies. It could also involve loading or initializing game resources specific to the gameplay phase.
- `update(self)`: The core game loop for the gameplay state, handling event processing, updating the state of the game world (including the player, enemies, and other entities), and managing collisions. It checks for user inputs, updates entity positions and states, and handles the interactions between various game elements.
- `resolve_entity_collision(self, entity1, entity2)`: A method for resolving collisions between entities, such as the player and enemies. It includes basic logic to adjust the positions of the entities to reflect a collision response.
- `draw(self, screen)`: Renders the game world to the screen, including the level, player, and enemies. It's responsible for drawing all visual elements of the gameplay state to provide visual feedback to the player.
- `handle_event(self, events)`: Processes input events specific to the gameplay, such as player movement and actions. It includes handling global game controls, like pausing the game.

The `Gameplay` state is critical for encapsulating the interactive part of the game, ensuring the game's rules are followed, and providing a dynamic and engaging experience for the player. It manages the flow of the game, the game's logic, and the visual presentation of the game world.
"""

class Gameplay(GameState):
    """
    The Gameplay class is responsible for managing the core gameplay loop, 
    including player actions, enemy behavior, collision detection, and game level progression. 
    It inherits from GameState and overrides its methods to implement game-specific logic and rendering.

    Attributes:
        game (Game): The main game object which holds components like the asset manager and state manager.
        player (Player): The player's character within the game.
        enemies (list): A list of Enemy objects representing the adversaries in the game.
        level (Level): The current level of the game, handling the layout and progression.
        collision_manager (CollisionManager): Manages collisions between game entities.
    """
    
    def __init__(self, game):
        """
        Initializes the Gameplay state with necessary game entities and configurations.
        
        Parameters:
            game (Game): The main game object which provides access to shared resources and managers.
        """
        super().__init__(game)
        player_sprite = self.game.asset_manager.get_image("player")
        player_x = 800 / 2 - player_sprite.get_width() / 2
        player_y = 500 / 2 - player_sprite.get_height() / 2
        self.player = Player(player_x, player_y, player_sprite, 100)

        self.enemies = [Enemy(200, 150, self.game.asset_manager.get_image("enemy"), 50, ChasePlayerBehavior())]
        self.level = Level(self.game)
        self.level.load([
            "WWWWWWWWWWWWWWWW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WFFFFFFFFFFFFFFW",
            "WWWWWWWWWWWWWWWW",
        ])
        self.collision_manager = CollisionManager(self.level)

    def enter(self):
        """
        Prepares the Gameplay state upon entering. This could include loading resources,
        initializing entities, or resetting game variables.
        """
        pass

    def update(self):
        """
        Updates the game logic each frame, handling player input, updating entity states,
        and managing game progression.
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False
            else:
                self.player.handle_event(event)
        
        self.player.update(self.collision_manager)
        self.level.update()

        for enemy in self.enemies:
            enemy.update(self.player, self.collision_manager)
            if self.collision_manager.check_entity_collision(self.player, enemy):
                self.player.take_damage(10)
                self.resolve_entity_collision(self.player, enemy)

    def resolve_entity_collision(self, entity1, entity2):
        """
        Resolves collisions between two entities by adjusting their positions.
        
        Parameters:
            entity1 (Entity): The first entity involved in the collision.
            entity2 (Entity): The second entity involved in the collision.
        """
        # Basic collision resolution logic
        if entity1.rect.x < entity2.rect.x:
            entity1.rect.x -= 5
        else:
            entity1.rect.x += 5
        if entity1.rect.y < entity2.rect.y:
            entity1.rect.y -= 5
        else:
            entity1.rect.y += 5
        entity1.x, entity1.y = entity1.rect.topleft

    def draw(self, screen):
        """
        Draws the game state to the screen, rendering the level, player, and enemies.
        
        Parameters:
            screen (pygame.Surface): The screen surface to draw the game elements on.
        """
        screen.fill((0, 0, 0))
        self.level.draw(screen)
        self.player.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)

    def handle_event(self, events):
        """
        Handles player input events, such as movement commands and game state changes.
        
        Parameters:
            events (list): A list of events to be processed.
        """
        for event in events:
            self.player.handle_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state_manager.change_state("Pause")