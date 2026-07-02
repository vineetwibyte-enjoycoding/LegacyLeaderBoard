import random
import time
from itertools import combinations
 # this helps me find all possible combinations for the computer, so it seems smart


def typer(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)


def typei(text):
    typer(text)
    user_input = input()
    return user_input


def run_war_game(playercards, computercards):
    tablecards = []
    movesplayed = 0
    gamecomplete = False
    
    def refill_to(hand, amount):
        while len(hand) < amount and deckofcards:
            hand.append(deckofcards.pop(0))
            
    while not gamecomplete:
        movecomplete = False
        if len(playercards) < 2 or len(computercards) < 2:
            typer("Not enough cards to continue War. It's a tie!\n")
            refill_to(playercards, 7)
            refill_to(computercards, 7)
            return "tie"  # early stop if not enough cards

        while not movecomplete:
            cardp = playercards.pop(0)
            cardc = computercards.pop(0)
            tablecards.append(cardp)
            tablecards.append(cardc)

            if cards.index(cardp[1:]) > cards.index(cardc[1:]):
                typer(f"Player wins the round with {cardp} and {cardc}.\n")
                playercards.extend(tablecards)
                tablecards.clear()
                movecomplete = True
                movesplayed += 1
            elif cards.index(cardp[1:]) < cards.index(cardc[1:]):
                typer(f"Computer wins the round with {cardc} and {cardp}.\n")
                computercards.extend(tablecards)
                tablecards.clear()
                movecomplete = True
                movesplayed += 1
            else:
                typer("War!.\n")
                if len(playercards) < 4 or len(computercards) < 4:
                    typer("Not enough cards to continue War. It's a tie!\n")
                    half = len(tablecards) // 2
                    playercards.extend(tablecards[:half])
                    computercards.extend(tablecards[half:])
                    tablecards.clear()
                    refill_to(playercards, 7)
                    refill_to(computercards, 7)
                    return "tie"
                else:
                    tablecards.extend(playercards[:3])
                    tablecards.extend(computercards[:3])
                    del playercards[:3]
                    del computercards[:3]
            typer(
                f"Length of Player Cards: {len(playercards)}, Length of Computer Cards: {len(computercards)}, Length of Table Cards: {len(tablecards)}, Moves Played: {movesplayed}\n"
            )

        if movesplayed == 10:
            if len(playercards) > len(computercards):
                typer("Player wins War!\n")
                refill_to(playercards, 8)
                refill_to(computercards, 7)
                return "player"
                
            elif len(playercards) < len(computercards):
                typer("Computer wins War!\n")
                refill_to(playercards, 7)
                refill_to(computercards, 8)
                return "computer"
                
            else:
                typer("War tie!\n")
                half = len(tablecards) // 2
                playercards.extend(tablecards[:half])
                computercards.extend(tablecards[half:])
                tablecards.clear()
                refill_to(playercards, 7)
                refill_to(computercards, 7)
                return "tie"


def isuseful(card, hand):
    # check if card can be used to form a meld with other cards in hand
    for c1, c2 in combinations(hand, 2):
        if meldcheck([card, c1, c2]):
            return True
    return False


typer("Welcome to Rummy + Card Game War! This is a hybrid Rummy + War card game played with a standard 52-card deck plus a special joker card, 🤡, which is worth higher than an Ace, which is higher than a King. Each player starts with 7 cards, and the goal is to form melds — either a set of three cards of the same rank or a run of three consecutive cards of the same suit. Players take turns drawing from the deck or the discard pile, laying down valid melds, and discarding one card each turn. If a player attempts an invalid meld, it triggers a mini War game, where both players play cards in rounds to determine a winner who may receive bonus cards. The first player to form at least 2 melds including at least one run can declare Rummy and win. The computer also follows the same rules and can declare Rummy if it meets the conditions. The game ends either when a player successfully declares Rummy or when the deck runs out, in which case the winner is decided by meld counts.\n\n")
typer("Order of cards: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace, Joker, or as represented in game, 2, 3, 4, 5, 6, 7, 8, 9, X, J, Q, K, A, 🤡.\n\n")

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "X", "J", "Q", "K", "A", "🤡"]
suits = ["♣", "♦", "♥", "♠"]

deckofcards = []

for suit in suits:
    for card in cards:
        deckofcards.append(suit + card)

random.shuffle(deckofcards)

toss = random.choice(deckofcards)

if toss[0] == "♣" or toss[0] == "♥":
    typer("Player starts.\n")
    playerturn = True
else:
    typer("Computer starts.\n")
    playerturn = False

playercards = deckofcards[:7]

computercards = deckofcards[7:14]

movecomplete = False
gamecomplete = False

tablecards = []
tablemelds = []
playermelds = []
computermelds = []
discardpile = [deckofcards[14]]
deckofcards = deckofcards[15:]
rummy = True
movesplayed = 0


def meldcheck(cardlist):
    if len(cardlist) != 3:  # only allow 3-card melds 
        return False

    # Set: all cards same rank
    ranks = [c[1:] for c in cardlist]
    if ranks[0] == ranks[1] == ranks[2]:
        return True

    # Run: all cards same suit and consecutive ranks
    meldsuits = [c[0] for c in cardlist]
    if meldsuits[0] == meldsuits[1] == meldsuits[2]:
        idxs = [cards.index(c[1:]) for c in cardlist]
        idxs.sort()  # list in ascending order
        if idxs[0] + 1 == idxs[1] and idxs[1] + 1 == idxs[2]:
            return True

    return False


def cardscore(card, hand):
    # higher score means more useful card

    suit, rank = card[0], card[1:]
    score = 0

    # part of potential set
    samerank = [c for c in hand if c[1:] == rank]
    score = len(samerank)

    # part of potential run
    rankidx = cards.index(rank)
    for kk in [-2, -1, 1, 2]:
        for c in hand:
            if c[0] == suit and cards.index(c[1:]) == rankidx + kk:
                score += 1
    return score


def choosediscard(hand):
    # choose the least useful card to discard
    scores = [(cardscore(c, hand), c) for c in hand]
    scores.sort()  # lowest score first
    return scores[0][1]  # return the card with lowest score, remember it is a tuple so we must do scores[0][0] not scores[0]


while rummy and not gamecomplete:  # rummy
    if playerturn:
        typer(f"Player cards: {playercards}\n")
        typer(f"Discard pile: {discardpile}\n")
        typer(f"Table melds: {tablemelds}\n")
        typer("Player turn.\n")
        typer("1. Draw from deck.\n")
        typer("2. Draw from discard pile.\n")
        typer("3. Lay down melds.\n")
        typer("4. Declare Rummy.\n")
        choice = typei("Enter your choice: ")
        if choice == "1":  # draw from deck
            if len(deckofcards) == 0:
                typer("Deck is empty. Please choose a different option.\n")
                continue
            else:
                playercards.append(deckofcards.pop(0))
                typer(f"Player drew a card from the deck: {playercards[-1]}\n")
                if len(playercards)==0:
                    typer("Player has no cards left. No need to discard.\n")
                    playerturn=False
                    continue
                typer("Please discard a card.\n")
                typer(f"Your cards: {playercards}\n")
                while True:
                    try:
                        discard = typei(
                            f"Enter the index of the card to discard (Example: 0 is {playercards[0]}): "
                        )
                    except IndexError:
                        discard=typei(f"Enter the index of the card to discard (Example: 0 is your first card): ")
                    try:
                        discard = int(discard)
                        if discard < 0 or discard >= len(playercards):
                            typer("Invalid card index.\n")
                            continue
                        discardpile.insert(0, playercards.pop(discard))
                        typer(f"Player discarded: {discardpile[0]}\n")
                        break
                    except ValueError:
                        typer("Invalid input.\n")
                        continue
                playerturn = False
        elif choice == "2":  # draw from discard pile
            if len(discardpile) == 0:
                typer("Discard pile is empty. Please choose a different option.\n")
                continue
            else:
                playercards.append(discardpile.pop(0))
                typer(f"Player drew a card from the discard pile: {playercards[-1]}\n")
                typer(f'Player Cards {playercards}')
                if len(playercards)==0:
                    typer("Player has no cards left. No need to discard.\n")
                    playerturn=False
                    continue
                typer("Please discard a card.\n")
                while True:
                    try:
                        discard = typei(f"Enter the index of the card to discard (Example: 0 is {playercards[0]}): ")
                    except IndexError:
                        discard=typei(f"Enter the index of the card to discard (Example: 0 is your first card): ")
                    try:
                        discard = int(discard)
                        if discard < 0 or discard >= len(playercards):
                            typer("Invalid card index.\n")
                            continue
                        discardpile.insert(0, playercards.pop(discard))
                        typer(f"Player discarded: {discardpile[0]}\n")
                        break
                    except ValueError:
                        typer("Invalid input.\n")
                        continue

                playerturn = False

        elif choice == "3":
            typer(f"Your cards: {playercards}\n")
            try:
                typer(f"Enter the indexes of 3 cards for the meld (example: 0 2 5 is {playercards[0]}, {playercards[2]}, {playercards[5]})\n")
            except IndexError:
                typer(f"Enter the indexes of 3 cards for the meld (example: 0 2 5 is your first, third, and sixth cards)\n")

            selection = typei("Indexes: ")

            try:
                i, j, k = map(int, selection.split()) # map function applies int to each element in the list

                #  RULE 1: indexes must exist
                if (i < 0 or j < 0 or k < 0 or i >= len(playercards) or j >= len(playercards) or k >= len(playercards)):
                    
                    typer("Invalid card index.\n")
                    # trigger war on invalid meld (any non-meld)
                    typer("Invalid meld! WAR triggered!\n")
                    result = run_war_game(playercards, computercards)
                    
                    if result == "player":
                        typer("You won the War! Draw a bonus card.\n")
                        if deckofcards:
                            playercards.append(deckofcards.pop(0))
                    elif result == "computer":
                        typer("Computer won the War!\n")
                    continue

                #  RULE 2: cards must be different
                if len({i, j, k}) != 3:
                    typer("You must choose three different cards.\n")
                    typer("Invalid meld! WAR triggered!\n")
                    result = run_war_game(playercards, computercards)
                    
                    if result == "player":
                        typer("You won the War! Draw a bonus card.\n")
                        if deckofcards:
                            playercards.append(deckofcards.pop(0))
                    elif result == "computer":
                        typer("Computer won the War!\n")
                    continue

                meldattempt = [playercards[i], playercards[j], playercards[k]]

                if meldcheck(meldattempt):
                    typer("Valid meld!\n")

                    for index in sorted([i, j, k], reverse=True):
                        tablemelds.append(playercards.pop(index))
                    playermelds.append(meldattempt)

                    typer(f"Meld placed on table: {tablemelds}\n")
                    playerturn=False
                    
                else:
                    typer("Invalid meld! WAR triggered!\n")

                    result = run_war_game(playercards, computercards)

                    if result == "player":
                        typer("You won the War! Draw a bonus card.\n")
                        if deckofcards:
                            playercards.append(deckofcards.pop(0))
                            playerturn=False

                    elif result == "computer":
                        typer("Computer won the War!\n")
                        if deckofcards:
                            computercards.append(deckofcards.pop(0))
                        playerturn=False

            except:
                typer("Invalid input.\n")
                typer("Invalid meld! WAR triggered!\n")
                result = run_war_game(playercards, computercards)
                if result == "player":
                    typer("You won the War! Draw a bonus card.\n")
                    if deckofcards:
                        playercards.append(deckofcards.pop(0))
                elif result == "computer":
                    typer("Computer won the War!\n")

        elif choice == "4":
            typer("Declaring Rummy!\n")
            if len(playermelds) < 2:
                typer(
                    f"You need at least 2  melds to declare Rummy. You have {len(playermelds)} melds.\n"
                )
                continue  # go back to player turn
            else:
                runfound = False
                for meld in playermelds:
                    suitss = [c[0] for c in meld]
                    if suitss[0] == suitss[1] == suitss[2]:
                        idxs = [cards.index(c[1:]) for c in meld]
                        idxs.sort()  # list in ascending order
                        if idxs[0] + 1 == idxs[1] and idxs[1] + 1 == idxs[2]:
                            runfound = True
                            break
                if runfound:
                    rummy = False
                    typer("Player wins Rummy!\n")
                    gamecomplete = True
                else:
                    typer("You need at least one run to declare Rummy.\n")
                    result = run_war_game(playercards, computercards)
                    if result == "player":
                        typer("You won the War! Draw a bonus card.\n")
                        if deckofcards:
                            playercards.append(deckofcards.pop(0))
                    elif result == "computer":
                        typer("Computer won the War!\n")
                        if deckofcards:
                            computercards.append(deckofcards.pop(0))
                    continue
        else:
            typer("Invalid choice.\n")
            continue
        # Deck exhaustion check
        if len(deckofcards) == 0:
            typer("Deck is empty. Game ends by card count!\n")
            if len(playermelds) > len(computermelds):
                typer("Player wins!\n")
            elif len(playermelds) < len(computermelds):
                typer("Computer wins!\n")
            else:
                typer("Tie game!\n")
            gamecomplete = True

    else:
        # Computer's turn
        # -------------------
        # Check if computer can declare Rummy
        if len(computermelds) >= 2:
            runfound = False
            for meld in computermelds:
                suitss = [c[0] for c in meld]
                if suitss[0] == suitss[1] == suitss[2]:
                    idxs = [cards.index(c[1:]) for c in meld]
                    idxs.sort()
                    if idxs[0] + 1 == idxs[1] and idxs[1] + 1 == idxs[2]:
                        runfound = True
                        break
            if runfound:
                typer("Computer declares Rummy!\n")
                rummy = False
                gamecomplete = True
                continue

        meldplayed = False
        for comb in combinations(computercards, 3): # computer tries to find a meld
            if meldcheck(comb): # if meld is found
                typer(f"Computer laid down meld: {comb}\n")
                for card in comb: # remove cards from computer's hand and add to table melds
                    computercards.remove(card)
                    tablemelds.append(card)
                computermelds.append(comb)
                meldplayed = True
                break
        if not meldplayed:
            topdiscard = discardpile[0]
            if isuseful(topdiscard, computercards):
                computercards.append(discardpile.pop(0))
            else:
                if len(deckofcards) == 0:
                    computercards.append(discardpile.pop(0))
                else:
                    computercards.append(deckofcards.pop(0))
        typer("Computer has picked up a card.\n")
        leastvaluablecard = choosediscard(computercards)
        typer(f"Computer discarded: {leastvaluablecard}\n")
        discardpile.insert(0, leastvaluablecard)
        del computercards[computercards.index(leastvaluablecard)]
        playerturn = True

        # Deck exhaustion check
        if len(deckofcards) == 0:
            typer("Deck is empty. Game ends by card count!\n")
            if len(playermelds) > len(computermelds):
                typer("Player wins!\n")
            elif len(playermelds) < len(computermelds):
                typer("Computer wins!\n")
            else:
                typer("Tie game!\n")
            gamecomplete = True
