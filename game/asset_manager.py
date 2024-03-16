import pygame
import json

class AssetManager:
    """
    The AssetManager class is responsible for loading, storing, and providing access
    to game assets, such as images and sounds. It simplifies the process of managing
    these resources throughout the game.

    Attributes:
        images (dict): A dictionary storing loaded images, accessible by name.
        sounds (dict): A dictionary storing loaded sounds, accessible by name.
    """

    def __init__(self):
        """
        Initializes the AssetManager with empty dictionaries for images and sounds.
        """
        self.images = {}
        self.sounds = {}

    def load_image(self, name, path, size=None):
        """
        Loads an image from a given path and stores it under a specified name.
        Optionally resizes the image.

        Parameters:
            name (str): The name to store the loaded image under.
            path (str): The file path to the image to be loaded.
            size (tuple, optional): The desired size (width, height) to scale the image to.

        Returns:
            pygame.Surface: The loaded and optionally resized image.
        """
        if name not in self.images:
            image = pygame.image.load(path).convert_alpha()
            if size:
                image = pygame.transform.scale(image, size)
            self.images[name] = image
        return self.images[name]

    def get_image(self, name):
        """
        Retrieves a previously loaded image by name.

        Parameters:
            name (str): The name of the image to retrieve.

        Returns:
            pygame.Surface or None: The image if found, or None if not found.
        """
        return self.images.get(name)

    def load_sound(self, name, path):
        """
        Loads a sound from a given path and stores it under a specified name.

        Parameters:
            name (str): The name to store the loaded sound under.
            path (str): The file path to the sound to be loaded.

        Returns:
            pygame.mixer.Sound: The loaded sound.
        """
        if name not in self.sounds:
            sound = pygame.mixer.Sound(path)
            self.sounds[name] = sound
        return self.sounds[name]

    def get_sound(self, name):
        """
        Retrieves a previously loaded sound by name.

        Parameters:
            name (str): The name of the sound to retrieve.

        Returns:
            pygame.mixer.Sound or None: The sound if found, or None if not found.
        """
        return self.sounds.get(name)

    def load_assets(self, asset_list):
        """
        Loads multiple assets from a list of asset definitions. Each asset definition
        is a dictionary specifying the type, name, path, and optionally size for images.

        Parameters:
            asset_list (list of dict): A list of dictionaries, each representing an asset to load.
        """
        for asset in asset_list:
            if asset['type'] == 'image':
                size = (asset['width'], asset['height']) if 'width' in asset and 'height' in asset else None
                self.load_image(asset['name'], asset['path'], size)
            elif asset['type'] == 'sound':
                self.load_sound(asset['name'], asset['path'])

    def load_assets_from_config(self, config_path):
        """
        Loads assets defined in a JSON configuration file. The configuration file
        should contain a list of asset definitions similar to what `load_assets`
        expects.

        Parameters:
            config_path (str): The file path to the JSON configuration file defining assets.
        """
        with open(config_path, 'r') as f:
            asset_list = json.load(f)
            self.load_assets(asset_list)
