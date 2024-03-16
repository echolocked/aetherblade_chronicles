# src/main.py
import pygame
from game.game_engine import GameEngine
from game.game_state import GameState
from rendering.state_renderer import StateRenderer
from rendering.image_loader import ImageLoader
from config import TILE_SIZE

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Aetherblade Chronicles")

    # Initialize the level and renderer
    level_path = "data/levels/level_0.txt"
    game_state = GameState(level_path)
    image_loader = ImageLoader("images/")

    game_engine = GameEngine(screen, game_state, image_loader)  # Assuming you adjust Engine to accept level and renderer

    game_engine.run()

if __name__ == "__main__":
    main()
