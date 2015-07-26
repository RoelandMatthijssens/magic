from unittest import TestCase
from unittest.mock import Mock
from src.Zone import Zone

class testZone(TestCase):
	def setUp(self):
		self.zone = Zone('Graveyard')

	def testZoneCreation(self):
		pass

	def testThatAZoneHasAName(self):
		self.assertEqual('Graveyard', self.zone.name)

	def testThatZoneHasAnOwner(self):
		alice = Mock()
		self.zone.addOwner(alice)
		self.assertIn(alice, self.zone.owners)

	def testThatAZoneCanHaveMultipleOwner(self):
		zone = Zone("Exile")
		alice = Mock()
		bob = Mock()
		zone.addOwner(alice)
		zone.addOwner(bob)
		self.assertIn(alice, zone.owners)
		self.assertIn(bob, zone.owners)

	def testThatOwnershipIsBidirectional(self):
		player = Mock()
		self.zone.addOwner(player)
		player.addZone.assert_called_with(self.zone, addRecursively=False)

	def testThatAPlayerIsAddedNonRecursively(self):
		player = Mock()
		self.zone.addOwner(player, addRecursively=False)
		assert not player.addZone.called, "addOwner should not be called when creating the bidirectional relation"
