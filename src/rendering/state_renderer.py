import pygame
from config import TILE_SIZE, BORDER_THICKNESS

class StateRenderer:
    def __init__(self, screen, game_state, image_loader):
        self.screen = screen
        self.game_state = game_state
        self.image_loader = image_loader

    def render(self):

        # Render map tiles
        for y in range(self.game_state.map_size[0]):
            for x in range(self.game_state.map_size[1]):
                tile_number = self.game_state.map_matrix[y][x]
                image_file = self.get_image_file(tile_number)
                tile_image = self.image_loader.get_image(image_file)
                self.screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))

        # Render the enemies
        for enemy in self.game_state.enemies:
            enemy_image_file = self.get_enemy_file(enemy.type)
            enemy_image = self.image_loader.get_image(enemy_image_file)
            self.screen.blit(enemy_image, (enemy.position[0] * TILE_SIZE, enemy.position[1] * TILE_SIZE))

        # Render the heroes
        for hero in self.game_state.heroes:
            hero_image_file = self.get_hero_file(hero.type)
            hero_image = self.image_loader.get_image(hero_image_file)
            self.screen.blit(hero_image, (hero.position[0] * TILE_SIZE, hero.position[1] * TILE_SIZE))

        # Render the cursor
        x, y = self.game_state.get_cursor_tile_position()
        pygame.draw.rect(self.screen, self.game_state.cursor_color, (x, y, TILE_SIZE, TILE_SIZE), BORDER_THICKNESS)


    def get_image_file(self, tile_number):
        # Map tile numbers to image filenames
        mapping = {
            0: "grass_light.png",
            1: "big_tree.png",
            # Add more mappings as necessary
        }
        return mapping.get(tile_number, "default.png")

    def get_enemy_file(self, type):
        # Mapping of enemy types to their corresponding image filenames
        enemy_mapping = {
            'Orc': 'orc.png',
            'Goblin': 'goblin.png',
            # Add more mappings as necessary
        }
        return enemy_mapping.get(type, 'default_enemy.png')
    
    def get_hero_file(self, type):
        # Mapping of heroes types to their corresponding image filenames
        hero_mapping = {
            'Alice': 'player1.png',
            'Eric': 'player2.png',
            # Add more mappings as necessary
        }
        return hero_mapping.get(type, 'default_hero.png')