import pygame
from pathlib import Path
from config import TILE_SIZE

class ImageLoader:
    def __init__(self, image_dir):
        self.image_dir = Path(image_dir)
        self.images = {}

    def get_image(self, filename):
        if filename not in self.images:
            image_path = self.image_dir / filename
            image = pygame.image.load(str(image_path)).convert_alpha()
            image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
            self.images[filename] = image
        return self.images[filename]