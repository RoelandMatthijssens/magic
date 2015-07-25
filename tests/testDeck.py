from unittest import TestCase
from unittest.mock import Mock
from src.Deck import Deck


class testDeck(TestCase):
	def setUp(self):
		self.deck = Deck()

	def testDeckCreation(self):
		pass

	def testThatCardsCanBeAdded(self):
		card = Mock()
		self.deck.addCard(card)
		self.assertIn(card, self.deck.cards)