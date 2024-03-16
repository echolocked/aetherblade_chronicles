# skills/base_skill.py

class BaseSkill:
    def __init__(self, name, description, cooldown, cost, range, effect):
        self.name = name  # The name of the skill
        self.description = description  # A brief description of what the skill does
        self.cooldown = cooldown  # The number of turns before the skill can be used again
        self.cost = cost  # The resource cost to use the skill, e.g., mana, energy, etc.
        self.range = range  # The effective range of the skill
        self.effect = effect  # The effect of the skill, could be a function or a predefined result

    def activate(self, user, target):
        """
        Activate the skill, applying its effect from the user to the target.
        This method should be overridden by subclasses for specific skill effects.
        """
        raise NotImplementedError("This method should be overridden by subclass")

    def is_available(self):
        """
        Check if the skill is available to be used based on cooldown, cost, or other conditions.
        This method can be customized in subclasses.
        """
        # Placeholder logic; implement your own availability conditions
        return self.cooldown == 0

    # You can include more methods that are common across all skills or necessary for your game's mechanics
