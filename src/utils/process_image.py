from PIL import Image
import os

print(os.getcwd())
image_path = './images/pixel_collection.png'
full_image = Image.open(image_path)

tile_width = 16
tile_count_vertical = full_image.height // tile_width
tile_count_horizontal = full_image.width // tile_width

# Function to save each tile image separately
def save_tiles(image, tile_width, tile_count_horizontal, tile_count_vertical):
    tiles = []
    for i in range(tile_count_vertical):
        for j in range(tile_count_horizontal):
            # Calculate the bounding box of the tile
            left = j * tile_width
            top = i * tile_width
            right = (j + 1) * tile_width
            bottom = (i + 1) * tile_width
            box = (left, top, right, bottom)
            
            # Crop the tile out of the full image and save it
            tile = image.crop(box)
            tile_path = f'./images/tile_{i}_{j}.png'
            tile.save(tile_path)
            tiles.append(tile_path)
    
    return tiles

# Save the tiles
tile_paths = save_tiles(full_image, tile_width, tile_count_horizontal, tile_count_vertical)
tile_paths