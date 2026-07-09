import csv
import random
from colorama import Fore
import os
import time
#imports

#Opening and reading elements.csv file(stored in computer)
with open('Elements_Revised.csv', mode='r') as file:
    csvFile = csv.DictReader(file)
    #allcards - a list of dictionaries(cards)
    allcards = list(csvFile)

#differentiating between irrelevant(cannot be measured) and relevant keys
relevantkeys = []
irrelevantkeys = ['Individual', 'Symbol']
allkeys = list(allcards[0].keys())
relevantkeys = list(allcards[0].keys())
relevantkeys.remove('Individual')
relevantkeys.remove('Symbol')


#code to display the card
def displaycard(card):
    count = 1
    maxvaluecharacters = 0
    maxcharacters = 40
    for key in allkeys:
        if maxvaluecharacters < len(card[key]):
            maxvaluecharacters = len(card[key]) + 5
            lenall = maxcharacters + maxvaluecharacters + 5
            #creating top line
    print(Fore.RESET + '━' * lenall)
    for key in allkeys:
        maxcharacters = 40
        characters = maxcharacters - len(key)

        #code for keys and values
        if key not in irrelevantkeys:
            print(Fore.RESET + '┃ ', end='')
            print(Fore.RESET + str(count) + '.' + key, end='')
            print(' ' * characters, end='')
            print(Fore.RESET + card[key], end='')
            valuecharacters = maxvaluecharacters - len(card[key])
            print(' ' * valuecharacters, end='')
            print(Fore.RESET + '┃', end='')
            print('')
            count = count + 1
        #coloring irrelevant keys and values differently
        else:
            print(Fore.RESET + '┃ ', end='')
            print(Fore.RED + key, end='')
            print(' ' * characters, end='')
            print(Fore.RED + ' ' * 2 + card[key], end='')
            valuecharacters = maxvaluecharacters - len(card[key])
            print(' ' * valuecharacters, end='')
            print(Fore.RESET + '┃', end='')
            print('')
    print(Fore.RESET + '━' * lenall)


#to determine winner every round
def playerwinner(player, computer, greatless):
    if greatless == 'greater':
        if player > computer:
            return True
        elif player < computer:
            return False
        else:
            return 'Draw'
    elif greatless == 'lesser':
        if player < computer:
            return True
        elif player > computer:
            return False
        else:
            return 'Draw'


#to determine winner every round
def compwinner(player, computer, greatless):
    if greatless == 'greater':
        if computer > player:
            return True
        elif computer < player:
            return False
        else:
            return 'Draw'
    elif greatless == 'lesser':
        if computer < player:
            return True
        elif computer > player:
            return False
        else:
            return 'Draw'


#shuffles and deals cards
random.shuffle(allcards)
playercards = allcards[1::2]
computercards = allcards[::2]

chance = 'P'
GameOver = False

#game script
while not GameOver:
    print('Player cards:', len(playercards))
    print('Computer cards:', len(computercards), '\n')
    #player's turn
    if chance == 'P' and len(playercards) > 0:
        PlayWin = False
        CompWin = False
        Draw = False
        table_cards = []

        play = playercards[0]
        playercards.pop(0)

        print(Fore.BLUE + 'PLAYER CARD')

        displaycard(play)

        chance = 'C'
        comp = computercards[0]
        computercards.pop(0)

        #appends player's and computer's cards to the table
        table_cards.append(play)
        table_cards.append(comp)

        #for the input of the category
        Answer = input(
            '\nWhich category would you like to compete with?(Type the number excluding the immeasureable units)(After that enter < or > to specify if you think it is greater or lesser than you opponents)\n'
        )
        selection = relevantkeys[int(Answer) - 1]

        playerval = play[selection]
        computerval = comp[selection]

        #for discovery date, few values are in BC. I have made BC values negative to overcome this
        if playerval.endswith('BC'):
            BC = playerval.split()
            playerval = '-' + BC[0]
        if computerval.endswith('BC'):
            BC = computerval.split()
            computerval = '-' + BC[0]

        #asking user to define greater or less instead of coding it
        answergreatless = input(
            '\nWill it be greater to less than your opponent\'s?(lesser < or > greater)\n'
        )
        mappingdict = {'<': 'lesser', '>': 'greater'}

        if playerwinner(playerval, computerval,
                        mappingdict[answergreatless]) == True:
            PlayWin = True
        elif playerwinner(playerval, computerval,
                          mappingdict[answergreatless]) == False:
            CompWin = True
        else:
            Draw = True

        #presenting who won by show both player's and computer's cards
        time.sleep(2)
        os.system('cls')
        print('Here is your card')
        time.sleep(1)
        displaycard(play)
        print('You chose', selection, '\n\n')
        time.sleep(4)
        print('Here is the computer\'s card:')
        time.sleep(3)
        displaycard(comp)
        print()
        time.sleep(1)
        if PlayWin == True:
            print('Player Wins!')
            playercards.extend(table_cards)
            table_cards.clear()
        elif CompWin == True:
            print('Computer Wins!')
            computercards.extend(table_cards)
            table_cards.clear()
        elif Draw == True:
            print('Draw!')
            table_cards.clear()
        time.sleep(5)
        os.system('cls')

    #computer's turn
    elif chance == 'C':
        tablecards = []

        play = playercards[0]
        playercards.pop(0)
        comp = computercards[0]
        computercards.pop(0)
        table_cards.append(play)
        table_cards.append(comp)

        chance = 'P'

        selection = random.choice(relevantkeys)
        playerval = play[selection]
        computerval = comp[selection]

        #for discovery date, few values are in BC. I have made BC values negative to overcome this
        if playerval.endswith('BC'):
            BC = playerval.split()
            playerval = '-' + BC[0]
        if computerval.endswith('BC'):
            BC = computerval.split()
            computerval = '-' + BC[0]

        list = ['0', '1']
        mappingdict = {'0': '<', '1': '>'}
        map = random.choice(list)
        answergreatless = mappingdict[map]

        if compwinner(playerval, computerval, answergreatless) == True:
            CompWin = True
        elif compwinner(playerval, computerval, answergreatless) == False:
            PlayWin = True
        else:
            Draw = True

        time.sleep(2)
        os.system('cls')
        print('Here is your card')
        time.sleep(1)
        displaycard(play)
        print('Computer chose', selection, 'and thought it to be',
              answergreatless, 'than yours.', '\n\n')
        time.sleep(4)
        print('Here is the computer\'s card:')
        time.sleep(1)
        displaycard(comp)
        print()
        time.sleep(3)
        if PlayWin == True:
            print('Player Wins!')
            playercards.extend(table_cards)
            table_cards.clear()
        elif CompWin == True:
            print('Computer Wins!')
            computercards.extend(table_cards)
            table_cards.clear()
        elif Draw == True:
            print('Draw!')
            table_cards.clear()
        time.sleep(5)
        os.system('cls')
