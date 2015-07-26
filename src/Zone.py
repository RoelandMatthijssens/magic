class Zone:
	def __init__(self, name):
		self.owners = []
		self.name = name

	def addOwner(self, player, addRecursively=True):
		self.owners.append(player)
		if addRecursively:
			player.addZone(self, addRecursively=False)