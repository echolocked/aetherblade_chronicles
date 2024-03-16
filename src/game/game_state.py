from units.enemy_troop_unit import EnemyTroopUnit
from units.player_hero_unit import PlayerHeroUnit
from vocations.base_vocation import BaseVocation
from config import TILE_SIZE

class LevelMap:
    def __init__(self, map_size, map_matrix):
        self.map_size = map_size
        self.map_matrix = map_matrix

class GameState:
    def __init__(self, file_path):
        self.file_path = file_path
        self.level_number = int(file_path.split('_')[-1].split('.')[0])
        self.map_size = (0, 0)
        self.map_matrix = []
        self.num_heroes = 0
        self.heroes = []
        self.num_enemies = 0
        self.enemies = []
        self.load_state(file_path)
        self.selected_unit = None
        self.running = True
        self.cursor_position = (0, 0)
        self.cursor_color = (255, 255, 0)
        self.current_phase = None

    def load_state(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # First line: size of the map (n, m)
            size_line = lines[0].strip()
            n, m = map(int, size_line.split(','))
            self.map_size = (n, m)

            # Next n lines: n x m matrix representing the map
            self.map_matrix = [list(map(int, line.strip().split())) for line in lines[1:n+1]]

            self.num_enemies = int(lines[n+1].strip())

            for line in lines[n+2:n+2+self.num_enemies]:
                enemy_data = line.strip().split(',')
                if len(enemy_data) >= 6:  # Basic validation
                    enemy_type = enemy_data[0]
                    position = (int(enemy_data[1]), int(enemy_data[2]))
                    hp = int(enemy_data[3])
                    attack = int(enemy_data[4])
                    defense = int(enemy_data[5])
                    attack_range = int(enemy_data[6])
                    element = enemy_data[7]
                    # TODO: Add concrete vocation class
                    vocation = BaseVocation(enemy_data[8], 1, 1, 2)
                    additional_attributes = enemy_data[9:]

                    enemy = EnemyTroopUnit(enemy_type, position, hp, attack, defense, attack_range, element, vocation, *additional_attributes)
                    self.enemies.append(enemy)

            self.num_heroes = int(lines[n+2+self.num_enemies].strip())

            for line in lines[n+3+self.num_enemies:n+3+self.num_enemies+self.num_heroes]:
                hero_data = line.strip().split(',')
                if len(hero_data) >= 6:  # Basic validation
                    hero_type = hero_data[0]
                    position = (int(hero_data[1]), int(hero_data[2]))
                    hp = int(hero_data[3])
                    attack = int(hero_data[4])
                    defense = int(hero_data[5])
                    attack_range = int(hero_data[6])
                    element = hero_data[7]
                    # TODO: Add concrete vocation class
                    vocation = BaseVocation(hero_data[8], 1, 1, 2)
                    additional_attributes = hero_data[9:]

                    hero = PlayerHeroUnit(hero_type, position, hp, attack, defense, attack_range, element, vocation, *additional_attributes)
                    self.heroes.append(hero)

    def display_map(self):
        for row in self.map_matrix:
            print(' '.join(map(str, row)))

    def display_enemies(self):
        for enemy in self.enemies:
            print(enemy)

    def get_unit_at(self, position):
        for unit in self.heroes + self.enemies:
            if unit.position == position:
                return unit
        return None
    
    def get_unit_at_cursor(self):
        return self.get_unit_at(self.cursor_position)
    
    def get_cursor_tile_position(self):
        return (self.cursor_position[0] * TILE_SIZE, self.cursor_position[1] * TILE_SIZE)
    
    def move_unit(self, unit, new_position):
        unit.position = new_position
