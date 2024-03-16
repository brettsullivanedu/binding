import pygame
import json

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}

    def load_image(self, name, path, size=None):
        if name not in self.images:
            image = pygame.image.load(path).convert_alpha()
            if size:
                # `size` is expected to be a tuple (width, height)
                image = pygame.transform.scale(image, size)
            self.images[name] = image
        return self.images[name]

    def get_image(self, name):
        return self.images.get(name)

    def load_sound(self, name, path):
        if name not in self.sounds:
            sound = pygame.mixer.Sound(path)
            self.sounds[name] = sound
        return self.sounds[name]

    def get_sound(self, name):
        return self.sounds.get(name)

    def load_assets(self, asset_list):
        """Load multiple assets from a list of asset definitions."""
        for asset in asset_list:
            if asset['type'] == 'image':
                size = (asset['width'], asset['height']) if 'width' in asset and 'height' in asset else None
                self.load_image(asset['name'], asset['path'], size)
            elif asset['type'] == 'sound':
                self.load_sound(asset['name'], asset['path'])

    def load_assets_from_config(self, config_path):
        """Load assets defined in a JSON configuration file."""
        with open(config_path, 'r') as f:
            asset_list = json.load(f)
            self.load_assets(asset_list)
