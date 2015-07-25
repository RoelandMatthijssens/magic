from unittest import TestCase
from unittest.mock import Mock
from src.Player import Player


class testPlayer(TestCase):
	def setUp(self):
		self.player = Player("Alice")

	def testThatThePlayerHasAName(self):
		self.assertEqual("Alice", self.player.name)