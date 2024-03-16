# elements/fire.py
from base_element import BaseElement

class Fire(BaseElement):
    def __init__(self):
        strengths = ["ice", "grass"]  # Example strengths
        weaknesses = ["water", "rock"]  # Example weaknesses
        super().__init__("fire", strengths, weaknesses)

    # You can add fire-specific methods or attributes here
