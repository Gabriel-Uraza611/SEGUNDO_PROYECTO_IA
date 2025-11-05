'''
card class
'''

class Card:
    """
    Represents a single card in the game.
    """

    def __init__(self, name: str, attack: int, defense: int, card_type: str = "normal"):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.card_type = card_type

    def __repr__(self):
        return f"{self.name} (ATK: {self.attack}, DEF: {self.defense})"

    def compare(self, other_card):
        """
        Compare this card to another one.
        Returns:
        - 1 if this card wins
        - -1 if this card loses
        - 0 if it's a tie
        """
        if self.attack > other_card.defense:
            return 1
        elif self.attack < other_card.defense:
            return -1
        else:
            return 0

