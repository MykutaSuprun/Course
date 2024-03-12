import csv

def read_game_scores(csv_filename):
    player_scores = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            player_scores.append((row['Player name'], int(row['Score'])))
    return player_scores

def create_high_scores_csv(player_scores, csv_filename):
    high_scores = {}

    for player, score in player_scores:
        if player not in high_scores or score > high_scores[player]:
            high_scores[player] = score

    sorted_high_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)

    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['Player name', 'Highest score']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for player, highest_score in sorted_high_scores:
            writer.writerow({'Player name': player, 'Highest score': highest_score})


game_scores = read_game_scores('game_scores.csv')


create_high_scores_csv(game_scores, 'high_scores.csv')
