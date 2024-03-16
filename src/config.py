from pathlib import Path

TILE_SIZE = 64
BORDER_THICKNESS = 2

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data"
IMG_PATH = BASE_DIR / "images"
LEVEL_PATH = DATA_PATH / "levels"
