# equipments/base_equipment.py

class BaseEquipment:
    def __init__(self, attack_bonus, defense_bonus, move_bonus, min_equip_level, equip_vocations):
        self.attack_bonus = attack_bonus  # Additional attack provided by the equipment
        self.defense_bonus = defense_bonus  # Additional defense provided by the equipment
        self.move_bonus = move_bonus  # Movement bonus provided by the equipment
        self.min_equip_level = min_equip_level  # Minimum level required to equip
        self.equip_vocations = equip_vocations  # List of vocations that can equip this item

    # You can add more common methods related to equipment here
