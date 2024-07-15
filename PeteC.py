from Player import Player

class PeteC(Player):

    def player_1_move(self, card1: float, card2: float) -> float:
        if card1 > 0.5 or card2 > 0.5:
            return 5
        return 0

    def player_2_move(self, card1, card2, bet) -> bool:
        if card1 > 0.5 or card2 > 0.5 and bet < 15:
            return True
        return False

    def get_name(self) -> str:
        return "Pete C"