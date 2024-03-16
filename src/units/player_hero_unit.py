from units.base_unit import BaseUnit

class PlayerHeroUnit(BaseUnit):
    def __init__(self, type, position, hp, attack, defense, attack_range, element, vocation, *args, **kwargs):
        super().__init__(hp, attack, defense, attack_range, element, vocation, *args, **kwargs)
        self.type = type
        self.position = position