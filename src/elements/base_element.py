# elements/base_element.py

class BaseElement:
    def __init__(self, name, strengths, weaknesses):
        self.name = name  # Name of the element
        self.strengths = strengths  # List of elements this element is strong against
        self.weaknesses = weaknesses  # List of elements this element is weak against

    def interacts_with(self, other_element):
        """
        Determine the interaction between this element and another.
        Could be overridden by subclasses for specific behaviors.
        """
        if other_element.name in self.strengths:
            return "strong"
        elif other_element.name in self.weaknesses:
            return "weak"
        return "neutral"

    # You can include more methods or attributes relevant to all elements here
