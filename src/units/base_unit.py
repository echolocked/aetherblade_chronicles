from equipments.equipment_types import EquipmentType

class BaseUnit:
    def __init__(self, hp, attack, defense, attack_range, element, vocation, experience=0, level=1):
        self.hp = hp  # Health points of the unit
        self.attack = attack  # Attack power
        self.defense = defense  # Defensive strength
        self.attack_range = attack_range  # Range in which the unit can attack
        self.element = element  # Elemental affinity of the unit
        self.vocation = vocation  # Class/job of the unit
        self.experience = experience  # Current experience points
        self.level = level  # Current level

        # Learned skills will be a list of skill objects; initially empty
        self.learned_skills = []

        # Equipments: dictionary holding item objects or None if slot is empty
        self.equipments = {
            EquipmentType.WEAPON: None,
            EquipmentType.ARMOR: None,
            EquipmentType.HEADSET: None,
            EquipmentType.ACCESSORY: None
        }

    def equip_item(self, equip_type, item):
        """Equip an item to the unit."""
        if equip_type in self.equipments:
            self.equipments[equip_type] = item
        else:
            print(f"Invalid item type: {equip_type}")

    def unequip_item(self, equip_type):
        """Remove an item from the unit."""
        if equip_type in self.equipments:
            self.equipments[equip_type] = None
        else:
            print(f"Invalid item type: {equip_type}")

    def learn_skill(self, skill):
        """Add a new skill to the unit's learned skills."""
        self.learned_skills.append(skill)

    def level_up(self):
        """Increase the unit's level and potentially other attributes."""
        self.level += 1
        # Additional logic for attribute increases and skill acquisition can be added here

    # Add more methods as needed for game logic, like attacking, defending, etc.