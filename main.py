from game import NimGame
from player import Player
from controller import GameController

game = NimGame([3, 4, 5])

players = [
    Player(0, "Maria"),
    Player(1, "João")
]

controller = GameController(game, players)
controller.play()