import csv
import random

def simulate_game(players, rounds):
    player_scores = []

    for player in players:
        for _ in range(rounds):
            score = random.randint(0, 1000)
            player_scores.append((player, score))

    return player_scores

def save_to_csv(player_scores, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Player name', 'Score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for player, score in player_scores:
            writer.writerow({'Player name': player, 'Score': score})


players_list = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']


game_results = simulate_game(players_list, 100)


save_to_csv(game_results, 'game_scores.csv')
