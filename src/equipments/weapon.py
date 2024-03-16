from base_equipment import BaseEquipment
from weapon_types import WeaponType

class Weapon(BaseEquipment):
    def __init__(self, attack_bonus, defense_bonus, move_bonus, min_equip_level, equip_vocations, weapon_type):
        super().__init__(attack_bonus, defense_bonus, move_bonus, min_equip_level, equip_vocations)
        self.weapon_type = weapon_type  # Type of the weapon (e.g., sword, bow, staff, etc.)

class Sword(Weapon):
    def __init__(self, attack_bonus, defense_bonus, move_bonus, min_equip_level, equip_vocations):
        super().__init__(attack_bonus, defense_bonus, move_bonus, min_equip_level, equip_vocations, WeaponType.SWORD)