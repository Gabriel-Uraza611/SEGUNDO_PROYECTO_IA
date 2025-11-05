'''
card class
'''

class Card:
    """
    Represents a single card in the game.
    """

    def __init__(self, id: str, name: str, attack: int, defense: int, level: int):
        self.id = id # 
        self.name = name # el mago 
        self.attack = attack # 290
        self.defense = defense
        self.level = level

    def __repr__(self):
        return f"{self.name} (ATK: {self.attack}, DEF: {self.defense})"


