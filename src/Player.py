class Player:
	def __init__(self, name):
		self.name = name
		self.zones = []

	def addZone(self, zone, addRecursively=True):
		self.zones.append(zone)
		if addRecursively:
			zone.addOwner(self, addRecursively=False)