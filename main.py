from Player import Player
from RandomPlayer import RandomPlayer
import random
import matplotlib.pyplot as plt

ante = 1
num_rounds = 500

def run_game(p1: Player, p2: Player):
    p1_profits = 0
    p2_profits = 0
    for i in range(num_rounds * 2):
        p1_card1, p1_card2 = random.random(), random.random()
        p2_card1, p2_card2 = random.random(), random.random()
        bet = p1.player_1_move(p1_card1, p1_card2)
        call = p2.player_2_move(p2_card1, p2_card2, bet)
        if not call:
            p1_profits += ante
            p2_profits -= ante
        else:
            winner = 1 if max(p1_card1, p1_card2) > max(p2_card1, p2_card2) else 2
            if winner == 1:
                p1_profits += bet + ante
                p2_profits -= bet + ante
            else:
                p1_profits -= bet + ante
                p2_profits += bet + ante
        p1, p2 = p2, p1
        p1_profits, p2_profits = p2_profits, p1_profits
    return p1_profits, p2_profits

all_players = [RandomPlayer() for _ in range(10)]
profits = [0 for _ in range(len(all_players))]
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
print(sorted_list)

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


    