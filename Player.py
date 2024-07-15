from abc import ABC, abstractmethod
"""
This is the base class for a a poker player for the simplified poker game with the following rules:
1. Each player antes 1 dollar and is dealt two cards (random numbers between 0 and 1)
2. Player 1 can bet any amount they choose or check
3. Player 2 can call or fold
4. If player 2 calls, the player with the highest of the 4 cards wins the pot
"""

class Player(ABC):
    """
    The class you implement for your poker player
    """
    def __init__(self):
        self.name = self.get_name()

    @abstractmethod
    def player_1_move(self, card1: float, card2: float) -> float:
        """
        :param card1: the value for card 1
        :param card2: the value for card 2
        :returns: how much you would like to bet
        """
        pass
    
    @abstractmethod
    def player_2_move(self, card1: float, card2: float, bet1: float) -> bool:
        """
        :param card1: the value for card 1
        :param card2: the value for card 2
        :param bet1: the amount player 1 bet
        :returns: True if you would like to call, False if you would like to fold
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        :returns: return the name of your player here
        """
        pass