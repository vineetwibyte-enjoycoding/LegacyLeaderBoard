import random
import pyfiglet
import colorama
import time
from colorama import Fore, Back, Style


a=random.randint(1,100)
print('What version would you like to play? Pick only one version pleas :) Or else :(')
print('version 1: You guess the number and then you choose a number and I will guess it')
print('version 2: find the coordinates of the treasure')
print('version 3: version 1 but with letters')
print('version 4: version 1 but with something interesting called binary search')

answer = input("type 1 if you want ver 1, 2 if you want ver 2 and 3 if you want ver 3 etc... :")
if answer == '1':
  print('I' , sep='\r')
  time.sleep(0.5)
  print('I a' , sep='\r')
  time.sleep(0.5)
  print('I am' , sep='\r')
  time.sleep(0.5)
  print('I am t' , sep='\r')
  time.sleep(0.5)
  print('I am th' , sep='\r')
  time.sleep(0.5)
  print('I am thi' , sep='\r')
  time.sleep(0.5)
  print('I am thin' , sep='\r')
  time.sleep(0.5)
  print('I am think' , sep='\r')
  time.sleep(0.5)
  print('I am thinki' , sep='\r')
  time.sleep(0.5)
  print('I am thinkin' , sep='\r')
  time.sleep(0.5)
  print('I am thinking' , sep='\r')
  time.sleep(0.5)
  print('I am thinking o' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a n' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a nu' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a num' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a numb' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a numbe' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number b' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number be' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number bet' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number betw' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number betwe' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number betwee' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 a' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 an' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 1' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 10' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. C' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Ca' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can y' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can yo' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you g' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you gu' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you gue' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you gues' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you guess' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you guess i' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you guess it' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you guess it?' , sep='\r')
  time.sleep(0.5)
  print('I am thinking of a number between 1 and 100. Can you guess it?' , sep='\r')

  print()

  attempts = 0
  done  = False

  while not done:
    guess = int(input('Please enter a number of your guess:'))  
    attempts +=1

    if guess > a:
     print()
     print('My number is smaller than you guess.\n')

    if  guess < a:
     print()
     print('My number is bigger than you guess.\n')

    if guess == a:
     print()
     print('BINGO! and you took', attempts, 'attempts!\n')
     done = True

  #now user will try to guess a number and computer will try to guess it

  print()
  print()
  print('Now, that you have defeated me, it will be your turn to chews a number between 1 and a 100 and I will try to guess it(no cheating...)\n')
  print('Click enter to continue...')

  input()

  guess = 1
  attempts = 0
  guess_steps = 10
  prev_answer = ''

  done  = False
  answer = input('Is your number ' + str(guess) + '? (y = yes, l = larger and s = smaller)\n')
  attempts = attempts + 1


  if attempts > 1:
    if prev_answer != answer:
      guess_steps = guess_steps - 1

  prev_answer = answer

  if answer == 's' or answer == 'S':
    guess = guess - guess_steps
    if guess < 1:
      guess = 1

  if answer == 'l' or answer == 'L':
    guess = guess + guess_steps
    if guess > 100:
      guess = 100


  if answer == 'y' or answer == 'Y':
    print('BINGO! I got it')
    print('I guessed your number in', attempts, 'attempts!\n')
    done = True



if answer == '2':

   print()
   print()  
   x0 = random.randint(1,100)
   y0 = random.randint(1,100)
   print('we have to find the treasure in a 100x100 city and we neeed your help!')
   print('or else the aliens will invade the city!')


   attempts = 0

   done  = False
   while not done:
     guess = input('Guess the coordinates of the treasure (x, y), comma separated:\n')

     attempts +=1

     guess_l = guess.split(',')
     guess_x = int(guess_l[0])
     guess_y = int(guess_l[1])

     if guess_x == x0:
       if guess_y < y0:
         print('The treasure is located to the north (x is the same but y is higher)')
       if guess_y > y0:
         print('The treasure is located to the south (x is the same but y is lower)')
       if guess_y == y0:
         print('TARGET FOUND! you saved the world by finding the treasure!!! (and you took', attempts, 'trys in finding th treasure!)')
         print(Fore.YELLOW)
         result = pyfiglet.figlet_format("ALIENS WILL NOT INVADE!", font = "slant" )
         print(result)
         print(Fore.GREEN)
         print('message from aliens:')
         print('we surrender!!!')
         print()
         print()
         print()
         print('now you will set some coodinates and me I will try to find them')
         #now user wil set coordinates and computer will guess them
         print('type the coordinates of the treasure (x, y), comma separated:\n')
         print('ENTER to continue...')
         input()

         while not done:
           print(Fore.YELLOW)
           answer = input('Is your number ' + str(guess) + '? (y = yes, l = larger and s = smaller)\n')
           attempts = attempts + 1

           guess = [0, 0]
           attempts = 0
           guess_steps = [10, 10]
           prev_answer = ['','']
           xy = 'xy'

           done  = False

           while not done:
             print(Fore.WHITE)
             answer = input('Is the treasure at ' + str(guess[0]) + ',' + str(guess[1]) + '? (y = yes, l = larger and s = smaller) - letters pleas\n')
             attempts = attempts + 1

             for kk in range(2):
               if attempts > 1 and answer[kk] != prev_answer[kk]:
                  guess_steps[kk] = guess_steps[kk] - 1

               prev_answer[kk] = answer[kk]

               if answer[kk] == 's' or answer[kk] == 'S':
                guess[kk] = guess[kk] - guess_steps[kk]



               if answer[kk] == 'l' or answer == 'L':
                 guess[kk] = guess[kk] + guess_steps[kk]

               if answer[kk] == 'y' or answer == 'Y':
                 print('Locked on ' , xy[kk])

               if guess[kk] > 100:
                 guess[kk] = 100
               if guess[kk] < 1:
                 guess[kk] = 1


           if answer[0].lower() == 'y' and answer[1].lower() == 'y':
             print('BINGO! I got it')
             print('I guessed your number in', attempts, 'attempts!\n')
             done = True




     if guess_x < x0:
       if guess_y < y0:
         print('The treasure is located to the northeast (both x and y are higher)')
       if guess_y > y0:
         print('The treasure is located to the southeast (x is higher and y is lower)')
       if guess_y == y0:
         print('The treasure is located to the eastern side (x is higher and y is the same)')

     if guess_x > x0:
       if guess_y < y0:
         print('The treasure is located to the northwest area (x is lower and y is higher)')
       if guess_y > y0:
         print('The treasure is located to the southwest (both x and y are lower)')
       if guess_y == y0:
         print('The treasure is located around the western locations (x is higher and y is the same)')


if answer == '3':
   letters = 'abcdefghijklmnopqrstuvwxyz'
   chosen_letter = random.choice(letters)
   print()
   print('I have picked of a letter between a and z. Can you guess it?')

   print()
   done = False
   attempts = 0
   while not done:
     print()
     guess = input('Please enter a letter of your guess:')
     attempts +=1

     if guess > chosen_letter:
       print()
       print('my letter comes before your guess')

     if guess < chosen_letter:
       print()
       print('my letter comes after your guess')

     if guess == chosen_letter:
       print()
       print('BINGO! you did it so well, and you took', attempts, 'attempts to find it!\n')
       done = True

       print('Now your chance select a letter between a and z and I will try to guess it')
       print('Click enter to continue...')

       input()
       guess = 0
       attempts = 0
       guess_steps = 5
       prev_answer = ''

       done  = False
       while not done:
         answer = input('Is your letter ' + letters[guess] + '? (y = yes, a = comes after and b = comes before)\n')
         attempts = attempts + 1

         if attempts > 1:
           if prev_answer != answer:
             guess_steps = guess_steps - 1

         prev_answer = answer

         if answer == 'b' or answer == 'B':  
           guess = guess - guess_steps
         if answer == 'a' or answer == 'A':
           guess = guess + guess_steps

         if guess > 25:
           guess = 25
         if guess< 0:
           guess = 0

         if answer == 'y' or answer == 'Y':
           print()
           print('PERFECT! I got it!')
           print('I guessed your chosen letter in', attempts, 'attempts!\n')
           done = True

if answer == '4':
  print()
  print()
  print('I am thinking of a number between 1 and 100. Can you guess it?' , sep='\r')

  print()

  attempts = 0
  done  = False

  while not done:
    guess = int(input('Please enter a number of your guess:'))  
    attempts +=1

    if guess > a:
     print()
     print('My number is smaller than you guess.\n')

    if  guess < a:
     print()
     print('My number is bigger than you guess.\n')

    if guess == a:
     print()
     print('BINGO! and you took', attempts, 'attempts!\n')
     done = True


  print()
  print()
  print('Now it will be my turn to guess your number, you can chews your number to be a decimal of .5 e.g(49.5, 50.5, 76.5)I am going to be smart this time(by using binary search which is a very efficient way to find a number)')
  print('Click enter to continue...')

  input()

  done  = False
  attempts = 0
  low = 1
  high = 100

  while not done:
    guess = round(low + high)/2
    answer = input('Is your number ' + str(guess) + '? (y = yes, l = larger and s = smaller)\n')
    attempts = attempts + 1


    if answer == 's' or answer == 'S':
      high = guess

    if answer == 'l' or answer == 'L':
      low = guess

    if answer == 'y' or answer == 'Y':
      print('BINGO! I got it')
      print('I guessed your number in', attempts, 'attempts!\n')
      done = True
else:
 print('You did not choose a valid option')