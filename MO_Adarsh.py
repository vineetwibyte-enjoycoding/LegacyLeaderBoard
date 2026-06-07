#imports
import random
from colorama import Fore

print(Fore.GREEN, 'MISSING OPERATORS')
print(Fore.RESET)

#blue answer
def ask(question):
  print(question,end='')
  print(Fore.BLUE,end='')
  reply = input()
  print(Fore.RESET,end='')
  return reply

#choice of difficulty
numbers = []
runloop = True
while runloop:
  difficulty = ask('Choose a difficulty - 1, 2, 3, etc. \nDifficulty is the number of blanks. \n')
  if not difficulty.isdigit() or difficulty == '0':
    print(Fore.RED, '\nInvalid input')
    print(Fore.RESET)
  else:
    difficulty = int(difficulty)
    runloop = False

#choice to randomize numbers
runloop = True
while runloop:
  choice = ask('\nWould you like to randomize your numbers?\n')
  
  if choice.lower() == 'y' or choice.lower() == 'yes':
    runloop = False
    for i in range(int(difficulty)+1):
      numbers.append(random.randint(1,100))
    print('\nYour numbers are :')
    for j in range(int(difficulty)+1):
      print(Fore.BLUE,numbers[j], end = ' ')
    print(Fore.RESET)
    
  elif choice.lower() == 'n' or choice.lower() == 'no':
    cnt = 0
    print()
    numeric = True
    runloop = True
    while runloop:
      while cnt < int(difficulty) + 1:
        numeric = ask('Number'+str(cnt+1)+': ')
        if numeric.isdigit():
          numbers.append(int(numeric))
          runloop = False
          cnt += 1
        else:
          print(Fore.RED, 'Invalid value')
          print(Fore.RESET,end='')
          
  else:
    print(Fore.RED, '\nInvalid input')
    print(Fore.RESET,end='')

#repeated game loop
def gameloop():
  list_copy = []
  num_list = []

  #shuffle numbers
  mix = random.randint(0,len(numbers))
  for i in range(len(numbers)):
    list_copy.insert(mix,int(numbers[i]))
    num_list.insert(mix,int(numbers[i]))
    
  op_list = ('+','-','*')
  op = ''
  
  for i in range(difficulty):
    op =  op + op_list[random.randint(0,2)]
  rhs = 0 
  
  def CheckAnswer(numberlist, operator):

    #multiplication first
    cnt = 0
    for i in range(difficulty):
      if operator[i] == '*':
        numberlist.insert(i-cnt, int(numberlist[i-cnt]) * int(numberlist[i+1-cnt]))
        numberlist.remove(numberlist[i+1-cnt])
        numberlist.remove(numberlist[i+1-cnt])  
        cnt+=1

    #addition and subtraction
    for i in range(difficulty):
      
      if operator[i] == '+':
        numberlist.insert(0,numberlist[0] + numberlist[1])
        numberlist.remove(numberlist[1])
        numberlist.remove(numberlist[1])
        
      if operator[i] == '-':
        numberlist.insert(0,numberlist[0] - numberlist[1])
        numberlist.remove(numberlist[1])
        numberlist.remove(numberlist[1])
    return numberlist[0]
    
  rhs = CheckAnswer(num_list, op)
  
  print('\nFill the missing op.')
  print(Fore.YELLOW, 'Eg: +, -*, **+.\n')
  print(Fore.RESET,end='')

  #question line
  print(Fore.GREEN,str(list_copy[0]), end = '')
  for i in range(difficulty):
    print(' __', str(list_copy[i+1]), end = ' ')  
  print(' = ',  str(rhs))
  print(Fore.RESET,end='')

  #list of remarks
  correct = ['Good Job!', 'Well Done.', 'Nice!']
  wrong = ['Wrong Answer.', 'Oops!', 'Incorrect.']
  answer = ask('\nYour answer: ')
  print()

  #check if the aanswer is valid
  check = 0
  runloop = True
  while runloop:
    if len(answer) == len(op): 
      #re-check
      check = CheckAnswer(list_copy, answer)
      runloop = False
    else:
      print(Fore.RED, '\nInvalid answer')
      print(Fore.RESET)
      answer = ask('Your answer: ')
  runloop = True

  #if answer is correct.
  if str(rhs) == str(check):
    print(Fore.YELLOW,end='')
    print('\n',correct[random.randint(0,2)])
    print(Fore.RESET, '\n-->')
    gameloop()
  else:
    print(Fore.RED)
    print(wrong[random.randint(0,2)])
    print('The answer was: ' + op)
    
gameloop()