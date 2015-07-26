from unittest import TestCase
from unittest.mock import Mock
from src.Player import Player


class testPlayer(TestCase):
	def setUp(self):
		self.player = Player("Alice")

	def testThatThePlayerHasAName(self):
		self.assertEqual("Alice", self.player.name)

	def testThatAPlayerCanOwnZones(self):
		graveyard = Mock()
		self.player.addZone(graveyard)
		self.assertIn(graveyard, self.player.zones)

	def testThatAddingAZoneAlsoGivesOwnership(self):
		zone = Mock()
		self.player.addZone(zone)
		zone.addOwner.assert_called_with(self.player, addRecursively=False)

	def testThatAZoneIsAddedNonRecursively(self):
		zone = Mock()
		self.player.addZone(zone, addRecursively=False)
		assert not zone.addOwner.called, "addOwner should not be called when creating the bidirectional relation"
