import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 8)
        self.card2 = Card("Clubs", 1)
        self.cards = [self.card1, self.card2]
        self.card_game = CardGame()
        self.card3 = Card("Spades", 8)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card3)
        self.assertEqual(None, result)

    
    def test_check_for_ace_false(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(False, result)

    def test_check_for_ace_true(self):
        result = self.card_game.check_for_ace(self.card2)
        self.assertEqual(True, result)
    
    
    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card1, result)

    def test_highest_card_equalvalues(self):
        result = self.card_game.highest_card(self.card1, self.card3)
        self.assertEqual(None, result)

    
    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 9", result)
