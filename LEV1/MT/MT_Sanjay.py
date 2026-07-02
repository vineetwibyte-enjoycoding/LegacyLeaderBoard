# Imports
import random
import time
from colorama import Fore

# Defining the animated text functions


def type(text):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.07)


def input_function(text):
  type(text)
  user_input = input()
  return user_input


# Starting the game
player_choice = ""
type(Fore.LIGHTMAGENTA_EX + "Hello there!\n")
player_name = input_function("What is your name? ")
type("Nice to meet you, " + player_name + "!" + "\n\n")
time.sleep(2)
type("Welcome to World War III" + "\n\n")
time.sleep(2)
type(
    "Your job- To help us win the war with a 3-round game of Rock-Paper-Scissors"
    + "\n\n")
time.sleep(2)
type("Are you ready?" + "\n\n")
time.sleep(2)

# Round 1
type(Fore.CYAN + "Round 1!" + "\n\n")
time.sleep(2)

valid_choice = False
player_score = 0
enemy_score = 0

# Checking for the validity of input
while not valid_choice:
  player_choice = input_function("Rock, Paper, or Scissors? ")
  if player_choice.capitalize() != "Rock" and player_choice.capitalize(
  ) != "Paper" and player_choice.capitalize() != "Scissors":
    type("\n")
    type("Not a valid choice. Type either Rock, Paper or Scissors!!\n\n")
  else:
    valid_choice = True

type(Fore.LIGHTRED_EX + "Your choice - " + player_choice.capitalize() + "\n\n")
type("Please wait as the enemy chooses...\n\n")
time.sleep(3)
enemy_choice = random.choice(["Rock", "Paper", "Scissors"])
type("The enemy has chosen - " + enemy_choice)
type("\n\n")

player_choice = player_choice.capitalize()
enemy_choice = enemy_choice.capitalize()

# Deciding the end result
if enemy_choice.capitalize() == player_choice.capitalize():
  type(Fore.BLUE + "That is a tie, 0-0\n\n")
  player_score = 0
  enemy_score = 0

elif (enemy_choice == "Rock" and player_choice == "Paper") or \
(enemy_choice == "Paper" and player_choice == "Scissors") or \
(enemy_choice == "Scissors" and player_choice == "Rock"):
  type(Fore.GREEN + "You win! 1-0\n\n")
  player_score = 1
  enemy_score = 0

else:
  type(Fore.RED + "You lose! 0-1\n\n")
  player_score = 0
  enemy_score = 1

# Round 2
time.sleep(2)
player_choice = ""
type(Fore.CYAN + "Round 2!" + "\n\n")
time.sleep(2)

valid_choice = False
# Checking for the validity of input
while not valid_choice:
  player_choice = input_function("Rock, Paper, or Scissors? ")
  if player_choice.capitalize() != "Rock" and player_choice.capitalize(
  ) != "Paper" and player_choice.capitalize() != "Scissors":
    type("\n")
    type("Not a valid choice. Type either Rock, Paper or Scissors!!\n\n")
  else:
    valid_choice = True

type(Fore.LIGHTRED_EX + "Your choice - " + player_choice.capitalize() + "\n\n")
type("Please wait as the enemy chooses...\n\n")
time.sleep(3)
enemy_choice = random.choice(["Rock", "Paper", "Scissors"])

type("The enemy has chosen - " + enemy_choice)
type("\n\n")

player_choice = player_choice.capitalize()
enemy_choice = enemy_choice.capitalize()

# Deciding the end result
if enemy_choice == player_choice:
  player_score += 0
  enemy_score += 0
  type(Fore.BLUE + "That is a tie, " + str(player_score) + "-" +
       str(enemy_score) + "\n\n")


elif (enemy_choice == "Rock" and player_choice == "Paper") or \
(enemy_choice == "Paper" and player_choice == "Scissors") or \
(enemy_choice == "Scissors" and player_choice == "Rock"):
  player_score += 1
  enemy_score += 0
  type(Fore.GREEN + "You win, " + str(player_score) + "-" + str(enemy_score) +
       "!" + "\n\n")

else:
  player_score += 0
  enemy_score += 1
  type(Fore.RED + "You lose, " + str(player_score) + "-" + str(enemy_score) +
       "!" + "\n\n")

time.sleep(2)
# Round 3
type(Fore.MAGENTA +
     "This is it, faithful warrior, the final round! Good luck!\n\n")
time.sleep(2)
type("You shall decide our fate, " + player_name + "!" + "\n\n")
time.sleep(2)
player_choice = ""
type(Fore.CYAN + "Round 3!" + "\n\n")
time.sleep(2)

valid_choice = False

while not valid_choice:
  player_choice = input_function("Rock, Paper, or Scissors? ")
  if player_choice.capitalize() != "Rock" and player_choice.capitalize(
  ) != "Paper" and player_choice.capitalize() != "Scissors":
    type("\n")
    type("Not a valid choice. Type either Rock, Paper or Scissors!!\n\n")
  else:
    valid_choice = True

type(Fore.LIGHTRED_EX + "Your choice - " + player_choice.capitalize() + "\n\n")
type("Please wait as the enemy chooses...\n\n")
time.sleep(3)
enemy_choice = random.choice(["Rock", "Paper", "Scissors"])
type("The enemy has chosen - " + enemy_choice)
type("\n\n")

player_choice = player_choice.capitalize()
enemy_choice = enemy_choice.capitalize()

# Deciding the end result
if enemy_choice == player_choice:
  player_score = player_score + 0
  enemy_score = enemy_score + 0
  type(Fore.BLUE + "That is a tie," + str(player_score) + "-" +
       str(enemy_score) + "\n\n")

elif (enemy_choice == "Rock" and player_choice == "Paper") or \
(enemy_choice == "Paper" and player_choice == "Scissors") or \
(enemy_choice == "Scissors" and player_choice == "Rock"):
  player_score = player_score + 1
  enemy_score = enemy_score + 0
  type(Fore.GREEN + "You win, " + str(player_score) + "-" + str(enemy_score) +
       "!" + "\n\n")

else:
  player_score += 0
  enemy_score += 1
  type(Fore.RED + "You lose, " + str(player_score) + "-" + str(enemy_score) +
       "!" + "\n\n")

time.sleep(2)
type(Fore.YELLOW + "The final score is " + str(player_score) + "-" +
     str(enemy_score) + "!" + "\n\n")
time.sleep(2)

# Determining the winner
if player_score > enemy_score:
  type(Fore.LIGHTGREEN_EX + "You win the war! Congratulations, " +
       player_name + "!\n\n")

if player_score < enemy_score:
  type(Fore.LIGHTRED_EX + "You lose the war! Better luck next time, " +
       player_name + "!\n\n")

if player_score == enemy_score:
  type(Fore.LIGHTCYAN_EX + player_name +
       ", you tied with the enemy! Better luck next time!\n\n")

time.sleep(2)

# Conclusion + Sign Off
type(Fore.LIGHTBLUE_EX + "Whew! That was a tough fight, " + player_name +
     "! Thanks for playing!\n\n")
time.sleep(2)
type(Fore.LIGHTYELLOW_EX + "Goodbye!\n\n")
quit()
# I really hope you enjoyed it as I took a lot of effort buiding this game. Thanks for playing 😊!