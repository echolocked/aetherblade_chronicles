# vocations/base_vocation.py

class BaseVocation:
    def __init__(self, name, growth_rate, base_attack_range, base_move):
        self.name = name  # The name of the vocation
        self.growth_rate = growth_rate  # Dict mapping stats (hp, attack, defense) to their growth rates
        self.base_attack_range = base_attack_range  # The basic attack range of this vocation
        self.base_move = base_move  # The base movement capability

        # Initialize more attributes if necessary
        self.skill_affinity = []  # Example: Types of skills or magic this vocation is proficient with

    def level_up(self):
        """
        Handle leveling up for a unit of this vocation. This method can be customized 
        for different vocations to account for varied growth rates or level-up bonuses.
        """
        # Example implementation (to be adjusted based on how units and stats are handled in your game):
        return {
            "hp_increase": self.growth_rate["hp"],
            "attack_increase": self.growth_rate["attack"],
            "defense_increase": self.growth_rate["defense"]
        }

    # Add more methods as necessary, like for unique vocation abilities, special moves, etc.
