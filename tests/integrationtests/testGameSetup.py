from unittest import TestCase
import itertools
from src.Card import Card
from src.Game import Game
from src.Player import Player
from src.Zone import Zone
from src.Deck import Deck


class testGameSetup(TestCase):

	def setupGame(self):
		players = self.createPlayers()
		zones = self.createZones()
		self.game = self.createGame(players, zones)

	def createPlayers(self):
		self.Alice = self.createPlayer("Alice")
		self.Bob = self.createPlayer("Bob")
		players = [self.Alice, self.Bob]
		return players

	def createPlayer(self, name):
		player = Player(name)
		deck = self.createDeck()
		player.deck = deck
		return player

	def createDeck(self):
		deck = Deck()
		for _ in itertools.repeat(None, 60):
			card = self.createCard()
			deck.addCard(card)
		return deck

	def createCard(self):
		card = Card()
		return card

	def createZones(self):
		AliceBattleField = Zone('Battlefield')
		BobBattleField = Zone('Battlefield')
		AliceGraveyard = Zone('Graveyard')
		BobGraveyard = Zone('Graveyard')
		AliceLibrary = Zone('Library')
		BobLibrary = Zone('Library')
		AliceHand = Zone('Hand')
		BobHand = Zone('Hand')
		AliceSideboard = Zone('Sideboard')
		BobSideboard = Zone('Sideboard')
		exile = Zone('Exile')
		aliceZones = [AliceBattleField, AliceGraveyard, AliceHand, AliceLibrary, AliceSideboard]
		bobZones = [BobBattleField, BobGraveyard, BobHand, BobLibrary, BobSideboard]
		sharedZones = [exile]
		for zone in aliceZones:
			zone.addOwner(self.Alice)
		for zone in bobZones:
			zone.addOwner(self.Bob)
		for zone in sharedZones:
			zone.addOwner(self.Alice)
			zone.addOwner(self.Bob)
		zones = aliceZones+bobZones+sharedZones
		return zones

	def createGame(self, players, zones):
		game = Game()
		for player in players: game.addPlayer(player)
		for zone in zones: game.addZone(zone)
		return game

	def setUp(self):
		self.setupGame()

	def testThatThereAreTwoPlayersInTheGame(self):
		players = self.game.players
		self.assertIn("Alice", [player.name for player in players])
		self.assertIn("Bob", [player.name for player in players])

	def testThatEachPlayerHasAGraveyard(self):
		aliceZoneNames = [zone.name for zone in self.Alice.zones]
		bobZoneNames = [zone.name for zone in self.Bob.zones]
		self.assertIn('Graveyard', aliceZoneNames)
		self.assertIn('Graveyard', bobZoneNames)