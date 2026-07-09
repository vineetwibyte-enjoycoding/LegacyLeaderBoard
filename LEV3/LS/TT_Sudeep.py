import csv
import random
from collections import Counter

with open('Football players.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    all_cards = list(csvFile)

relevant_keys = list(all_cards[0].keys())
relevant_keys = relevant_keys[3:]

def display_card(card):
    rarity = card['Rarity']
    max_chars = max(len(k) for k in card)
    print(f"Rarity: {rarity}")
    for key, value in card.items():
        if key != 'Rarity':
            print(f"{key:<{max_chars}} : {value}")

def determine_winner(m1, m2, rarity1, rarity2, table_cards, player_cards, comput_cards):
    winner = "draw"
    if m1 == m2:
        if rarity1 == "Legendary" and rarity2 != "Legendary":
            winner = "player"
        elif rarity2 == "Legendary" and rarity1 != "Legendary":
            winner = "computer"
    else:
        winner = "player" if m1 > m2 else "computer"
        if winner == "player":
            if rarity1 == "Rare":
                player_cards.extend(comput_cards[:2])
                comput_cards = comput_cards[2:]
            elif rarity1 == "Legendary":
                player_cards.extend(comput_cards[:5])
                comput_cards = comput_cards[5:]
        elif winner == "computer":
            if rarity2 == "Rare":
                comput_cards.extend(player_cards[:2])
                player_cards = player_cards[2:]
            elif rarity2 == "Legendary":
                comput_cards.extend(player_cards[:5])
                player_cards = player_cards[5:]

    return winner, player_cards, comput_cards

def assign_rarity(cards):
    for card in cards:
        rarity = random.choices(["Common", "Rare", "Legendary"], weights=[70, 25, 5])[0]
        card['Rarity'] = rarity

assign_rarity(all_cards)
random.shuffle(all_cards)
comput_cards = all_cards[0::2]
player_cards = all_cards[1::2]
table_cards = []

stats = {
    'rounds_won': {'player': 0, 'computer': 0},
    'longest_streak': {'player': 0, 'computer': 0},
    'current_streak': {'player': 0, 'computer': 0},
    'most_used_attribute': Counter()
}

game_over = False
chance = 'player'

while not game_over:
    print(f"Player cards: {len(player_cards)}, Computer cards: {len(comput_cards)}, Table cards: {len(table_cards)}")

    player = player_cards.pop(0)
    comput = comput_cards.pop(0)
    table_cards.extend([player, comput])

    if len(table_cards) > 24:
        table_cards = table_cards[:24]

    print("\nYour card:")
    display_card(player)
    

    if chance == 'player':
        print("Choose an attribute:")
        for idx, key in enumerate(relevant_keys):
            print(f"  {chr(65 + idx)} for {key}")
        player_choice = input("Your choice: ").upper()
        key_requested = relevant_keys[ord(player_choice) - 65] if player_choice.isalpha() else None
        if key_requested not in relevant_keys:
            print("Invalid choice! Try again.")
            continue
        stats['most_used_attribute'][key_requested] += 1
        chance = 'computer'
    else:
        key_requested = random.choice(relevant_keys)
        print(f"Computer chose: {key_requested}")
        chance = 'player'

    value_player = int(player[key_requested])
    value_comput = int(comput[key_requested])

    if player['Rarity'] == "Legendary":
        value_player += 5
    if comput['Rarity'] == "Legendary":
        value_comput += 5

    winner, player_cards, comput_cards = determine_winner(value_player, value_comput, 
                              player['Rarity'], comput['Rarity'], 
                              table_cards, player_cards, comput_cards)

    print(f"\nKey of interest: {key_requested}")
    print(f"Player's {key_requested}: {value_player} (Rarity: {player['Rarity']})")
    print(f"Computer's {key_requested}: {value_comput} (Rarity: {comput['Rarity']})")
    print(f"Winner: {winner.capitalize()}")

    if winner != 'draw':
        stats['rounds_won'][winner] += 1
        stats['current_streak'][winner] += 1
        other = 'player' if winner == 'computer' else 'computer'
        stats['current_streak'][other] = 0
        stats['longest_streak'][winner] = max(stats['longest_streak'][winner], stats['current_streak'][winner])

    if winner == "player":
        player_cards.extend(table_cards)
        table_cards.clear()
    elif winner == "computer":
        comput_cards.extend(table_cards)
        table_cards.clear()

    if len(player_cards) == 0:
        print("Computer won the game!")
        game_over = True
    elif len(comput_cards) == 0:
        print("Player won the game!")
        game_over = True

print("\nGame Over! Final Stats:")
print(f"Rounds Won - Player: {stats['rounds_won']['player']}, Computer: {stats['rounds_won']['computer']}")
print(f"Longest Winning Streak - Player: {stats['longest_streak']['player']}, Computer: {stats['longest_streak']['computer']}")
most_used = stats['most_used_attribute'].most_common(1)
if most_used:
    print(f"Most Used Attribute: {most_used[0][0]} ({most_used[0][1]} times)")
