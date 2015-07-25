from unittest import TestCase
from src.Zone import Zone

class testZone(TestCase):
	def testZoneCreation(self):
		zone = Zone('zoneName')