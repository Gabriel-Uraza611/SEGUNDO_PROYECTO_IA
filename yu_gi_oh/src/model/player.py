'''
Player class
'''
# model/player.py
from model.card import Card

class Player:
    """
    Represents a player (human or AI).
    """

    def __init__(self, name: str, is_human: bool = True):
        self.name = name
        self.is_human = is_human
        self.hand = []       # Cards in hand
        self.deck = []       # Cards yet to draw
        self.discard_pile = []  # Played or discarded cards

    def draw_card(self):
        """Draw a card from the deck and add it to the hand."""
        if self.deck:
            card = self.deck.pop(0)
            self.hand.append(card)
            return card
        return None

    def play_card(self, index: int):
        """Play a card from the hand by index."""
        if 0 <= index < len(self.hand):
            card = self.hand.pop(index)
            self.discard_pile.append(card)
            return card
        return None

    def __repr__(self):
        return f"Player({self.name}, cards in hand: {len(self.hand)})"
