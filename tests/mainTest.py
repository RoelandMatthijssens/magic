from unittest import TestCase
import itertools
from src.Card import Card
from src.Game import Game
from src.Player import Player
from src.Zone import Zone
from src.Deck import Deck


class testMain(TestCase):

	def testGameSetup(self):
		players = self.createPlayers()
		zones = self.createZones()
		game = self.createGame(players, zones)
		return game

	def createPlayers(self):
		Alice = self.createPlayer("Allice")
		Bob = self.createPlayer("Bob")
		players = [Alice, Bob]
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
		zones = [AliceBattleField, AliceGraveyard, AliceHand, AliceLibrary, AliceSideboard,
						 BobBattleField, BobGraveyard, BobHand, BobLibrary, BobSideboard,
						 exile]
		return zones

	def createGame(self, players, zones):
		game = Game()
		for player in players: game.addPlayer(player)
		for zone in zones: game.addZone(zone)
		return game
