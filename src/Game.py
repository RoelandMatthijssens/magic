class Game:
	def __init__(self):
		self.zones = []
		self.players = []
	def addZone(self, zone):
		self.zones.append(zone)
	def addPlayer(self, player):
		self.players.append(player)