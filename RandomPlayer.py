from Player import Player
import random

class RandomPlayer(Player):
    def __init__(self):
        pass

    def player_1_move(self, card1: float, card2: float) -> float:
        return random.uniform(0, 100)
    

    def player_2_move(self, card1, card2, bet) -> int:
        return random.choice([True, False])
    
    def get_name(self) -> str:
        return "Random Player " + str(random.randint(0, 100))