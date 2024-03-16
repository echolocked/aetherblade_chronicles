import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tile Painting with Grass and Trees')

# Load the grass and tree images
grass_image_path = './images/grass_light.png'  # Replace with your grass image file path
tree_image_path = './images/big_tree.png'   # Replace with your tree image file path
grass_tile = pygame.image.load(grass_image_path)
tree_tile = pygame.image.load(tree_image_path)

# Get the size of the tiles (assuming both have the same size)
tile_size = grass_tile.get_size()  # Get the size of the tile

# Define how frequently we want to scatter trees, e.g., 1 tree per 10 grass tiles
tree_frequency = 10

# The main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# Paint the grass tiles
for y in range(0, screen_height, tile_size[1]):
    for x in range(0, screen_width, tile_size[0]):
        screen.blit(grass_tile, (x, y))

# Randomly scatter trees
for y in range(0, screen_height, tile_size[1]):
    for x in range(0, screen_width, tile_size[0]):
        if random.randint(1, tree_frequency) == 1:  # Random chance to place a tree
            screen.blit(tree_tile, (x, y))

# Update the display
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()