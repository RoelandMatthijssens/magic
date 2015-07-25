from unittest import TestCase
from unittest.mock import Mock
from src.Game import Game

class testBoard(TestCase):
	def setUp(self):
		self.game = Game()

	def testThatAGameCanHaveZones(self):
		zone = Mock()
		self.game.addZone(zone)
		self.assertIn(zone, self.game.zones)

	def testThatAGameHasPlayers(self):
		player = Mock()
		self.game.addPlayer(player)
		self.assertIn(player, self.game.players)
