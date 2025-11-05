'''
deck of cards
'''
import random
from model.card import Card

class Deck:
    """
    Represents a deck of cards (the draw pile).
    """

    def __init__(self, cards=None):
        self.cards = cards if cards else []

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw(self):
        """Draw the top card from the deck."""
        return self.cards.pop(0) if self.cards else None

    def add_card(self, card: Card):
        """Add a card to the deck."""
        self.cards.append(card)

    def deal(self, players, starting_cards=5):
        """Deal starting cards to each player."""
        for _ in range(starting_cards):
            for player in players:
                if self.cards:
                    player.hand.append(self.draw())

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck({len(self.cards)} cards remaining)"
