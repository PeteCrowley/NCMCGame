from Player import Player
from RandomPlayer import RandomPlayer
import random
import matplotlib.pyplot as plt
from PeteC import PeteC


ante = 1            # ante is 1 dollar
num_rounds = 500    # each round has each player being player 1 and 2

def run_game(p1: Player, p2: Player):
    # Each player starts even
    p1_profits = 0
    p2_profits = 0
    for i in range(num_rounds * 2):
        # Deal two cards to each player
        p1_card1, p1_card2 = random.random(), random.random()
        p2_card1, p2_card2 = random.random(), random.random()
        # Player 1 bets according to their strategy
        bet = p1.player_1_move(p1_card1, p1_card2)
        # Player 2 calls or folds according to their strategy
        call = p2.player_2_move(p2_card1, p2_card2, bet)
        # A fold means player 1 wins the pot
        if not call:
            p1_profits += ante
            p2_profits -= ante
        else:
            # Winner is whoever has the highest card
            winner = 1 if max(p1_card1, p1_card2) > max(p2_card1, p2_card2) else 2
            # Player 1 wins the pot
            if winner == 1:
                p1_profits += bet + ante
                p2_profits -= bet + ante
            # Player 2 wins the pot
            else:
                p1_profits -= bet + ante
                p2_profits += bet + ante
        # Switch Player 1 and Player 2
        p1, p2 = p2, p1
        p1_profits, p2_profits = p2_profits, p1_profits
    # Reutrn the net profits of each player
    return p1_profits, p2_profits

# All players will go in this list
all_players = [RandomPlayer() for _ in range(9)] + [PeteC()]
profits = [0 for _ in range(len(all_players))]      # Everyone starts with 0 profits

# Round robin tournament, everyone plays everyone
for i in range(len(all_players)):
    for j in range(i + 1, len(all_players)):
        p1_profits, p2_profits = run_game(all_players[i], all_players[j])
        profits[i] += p1_profits
        profits[j] += p2_profits

# Get the names of all players
player_names = [player.get_name() for player in all_players]

# Combine the two lists into a list of tuples
combined_list = list(zip(player_names, profits))

# Sort the combined list by profits (second element of the tuple)
sorted_list = sorted(combined_list, key=lambda x: x[1])

# Separate the sorted list back into two lists
sorted_player_names, sorted_profits = zip(*sorted_list)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(sorted_player_names, sorted_profits, color='skyblue')
plt.xlabel('Player Names')
plt.ylabel('Profits')
plt.title('Player Profits')
plt.xticks(rotation=80)
plt.tight_layout()

# Show the plot
plt.show()


    