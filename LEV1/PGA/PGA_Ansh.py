import time
import datetime as dt
import colorama
import random
from colorama import Fore, Back, Style
print(Fore.WHITE + Back.CYAN + 'welcome to the game of quizes!!!')
print()
print(Back.LIGHTYELLOW_EX + 'Pleas choose a version to play (1/2/3):')
print(Back.YELLOW + 'Ver 1.  meet Valt Ahoy (beyblade quiz with grumpy blader)')
print(Back.GREEN + 'Ver 2.  meet the manager (English quiz with grumpy assistant)')
print(Back.BLUE + 'Ver 3. meet the smartest prof! (mix of subjects (even 1 question of pokemon) quiz with grumpy robot)')
answer = input('(1/2/3): ')
print(Back.RESET)
if answer == '1':
  ct1 = dt.datetime.now()
  print('beyblade quiz')
  print(Fore.RED + 'This is Japan the blading world!!!')
  print()
  print()
  print(Fore.YELLOW + 'you are a beginner blader and you want to become the best blader in the world right?')
  print('you got a new bay!!!!')
  print('your bay is called valtdrand')
  print(Fore.WHITE + 'you want to meet the worlds best bladers but you will first have to pass this quiz!!!')
  print()
  print('Well I am a blader to and you will first have to pass my quiz')
  print()
  print(Fore.GREEN + 'Q 1:')
  print()
  print(Fore.WHITE)
  answer = input('Hwo is the best blader in the world?\n')
  if answer.lower() == 'valt' or answer.lower() == 'valt ahoy':  
    print('That was just an easy warm up, it was to test your IQ in beblade...')
    
  else:
    print('How did you not know that, it was just a warm up?!')
    
  time.sleep(1)
  print()
  print(Fore.GREEN + 'Q 2:')
  print()
  print(Fore.WHITE)
  answer = input('Name me a series of beyblade (can be any but only one):')
  if answer.lower() == 'beyblade burst turbo':
    print('They\'ve alredy taken that series off Netflix so it\'s not very popular anymore.')
  elif answer.lower() == 'beyblade X':
    print('That one\'s to classical couldin\'t you have been a bit more creative?')
  elif answer.lower() == 'beyblade squad drive':
    print('Not many people like it so I won\'t accept your answer.')
  elif answer.lower() == 'beyblade burst evolution':
    print('I don\'t like that answer for some reason, so I won\'t accept it.') 
  else:
    print(Fore.RED + 'That\'s not a series of beyblade, be more smart next time please!')

  time.sleep(1)
  print()
  print(Fore.GREEN + 'Q 3:')
  print()
  print(Fore.WHITE)
  print('Name me the 2 real beyblades from these 6 options a beyblade (type the 2 put comma to seperate them, no space after comma):')

  print('A. valtdrand' , '    B. valtrieck 2.0' , sep = '\t\t')
  print('C. valtdrand 2.0' , 'D. valtryek' , sep = '\t\t')
  print('E. rocktavor' , '    F. entretian' , sep = '\t\t')
  answer = input()
  if answer.lower() == 'b,e':
    print('In these 6 options it was clear you would choose the correct ones, so don\'t be so proud of your self.')
  elif answer.lower() == 'a,f':
    print('You\'re so close to the answer, but you\'re still wrong looser.')
  elif answer.lower() == 'c,e':
    print('That was not close.')
  elif answer.lower() == 'a,b':
    print('It\'s not as easy as you think it is.')
  else:
    print('You\'re so bad at this, ofcorse it wasim\'t that, you should go back to your house and be disappointed of your self!')
  print()
  time.sleep(1)
  print(Fore.GREEN + 'Q 4:')
  print()
  print(Fore.WHITE)
  answer =input('who are is Valt\'s biggest rival?')
  if answer.lower() == 'aiger' or answer.lower() == 'aiger rockabone':
    print('That was a correct answer, but you have not finished yet.')
  elif answer.lower() == 'blayder X' or answer.lower() == 'free delahoya':
    print('No way, your wrong.')
  else:
    print('You are never going to be a blader if you don\'t even know who Valt\'s biggest rival is!')
  print()
  time.sleep(1)
  print(Fore.GREEN + 'Q 5 (FINAL ONE!!!):')
  print()
  print(Fore.WHITE)
  answer = input('Are you a blader?')
  if answer.lower() == 'yes':
    print('NO ONE EVER QUALIFIDE YOU AS A BLADER SO YOUR A LIAR!')
  elif answer.lower() == 'no':
    print('WELL IF YOU ARE NOT A BLADER GET OUT OF HERE YOU SUCKER!')
  else:
    print('Don\'t you even know how to answer a question!')
  ct2 = dt.datetime.now()
  diff = ct2 - ct1
  print()
  print('Wait Whaaaaat you took', diff.seconds, 'to complete the quiz, you are extra slow!')
  print('You think I have no other work ...')
  
if answer == '2':
  print()
  print(Fore.WHITE + 'you want to meet the manager right? Well first have to pass this quiz!!!')
  print()
  print(Fore.GREEN + 'Q 1:')
  print()
  time.sleep(0.5)
  answer = input(Fore.WHITE + 'what are action words called in English? ')
  ct1 = dt.datetime.now()
  furius = 0
  
  if answer.lower()  == 'verbs' or answer.lower() == 'verb':
    print()
    print('okay you may have got it correct, but that was just a warm up...')
    
  else:
    print()
    print(Fore.RED)
    print('That was completly wrong, YOU SHOULD HAVE READ THE QUESTION BETTER, and have you not been to school or what?')
    print('Let\'s see how well you do in the next question')
    print('The manager won\'t be impressed with you if you don\'t know the basics of english!')
    attempts =+ 1
    
  print()
  
  print(Fore.GREEN + 'Q 2:')
  print()
  print(Fore.WHITE)
  decider = random.randint(0, 2)

  if decider == 0:
    word = input('give me a word with 8 letters in English with at least 3 vowels: ')
  
    if len(word) == 8:
      print('Good that you got that part right but still...')
  
      count_a = word.count('a')
      count_e = word.count('e')
      count_i = word.count('i')
      count_o = word.count('o')
      count_u = word.count('u')
      print()
      count_vowels = count_a + count_e + count_i + count_o + count_u
      print('a,e,i,o,u')
      print(count_a, count_e, count_i, count_o, count_u)
  
      if count_vowels > 3:
        print(Fore.BLUE)
        print('OOOFF ... you\'ve got to many vowels in there, for me.')
        print('WHAT A WASTE OF TIME FROM YOU I HAD CLEARLY TOLD YOU 3 NOT MORE!')
      elif count_vowels < 3:
        print(Fore.LIGHTBLUE_EX)
        print('I told you to have atleast 3 vowels in there!')
        print('you should read more carefully!')
      else:
        print(Fore.WHITE)
        print('whaaaat only 3 vowels, realy?? That\'s so boring!')
        print(' Can\'t you be motivated? No congrats for you ... no extra effort niether!')
        
    if decider == 1:
      word = input('give me a word with 7 letters in English with at least 2 vowels: ')

      if len(word) == 7:
        print('Good that you got that part right but still...')

        count_a = word.count('a')
        count_e = word.count('e')
        count_i = word.count('i')
        count_o = word.count('o')
        count_u = word.count('u')
        print()
        count_vowels = count_a + count_e + count_i + count_o + count_u
        print('a,e,i,o,u')
        print(count_a, count_e, count_i, count_o, count_u)

        if count_vowels > 2:
          print(Fore.BLUE)
          print('OOOFF ... you\'ve got to many vowels in there, for me.')
          print('WHAT A WASTE OF TIME FROM YOU I HAD CLEARLY TOLD YOU 2 NOT MORE!')
        elif count_vowels < 2:
          print(Fore.LIGHTBLUE_EX)
          print('I told you to have atleast 2 vowels in there!')
          print('you should read more carefully!')
        else:
          print(Fore.WHITE)
          print('whaaaat only 2 vowels, realy?? That\'s so boring!')
          print(' Can\'t you be motivated? No congrats for you ... no extra effort niether!')

  if decider == 2:
    word = input('give me a word with 9 letters in English with at least 4 vowels: ')

    if len(word) == 9:
      print('Good that you got that part right but still...')

      count_a = word.count('a')
      count_e = word.count('e')
      count_i = word.count('i')
      count_o = word.count('o')
      count_u = word.count('u')        
      print()
      count_vowels = count_a + count_e + count_i + count_o + count_u
      print('a,e,i,o,u')
      print(count_a, count_e, count_i, count_o, count_u)

      if count_vowels > 4:
        print(Fore.BLUE)
        print('OOOFF ... you\'ve got to many vowels in there, for me.')
        print('WHAT A WASTE OF TIME FROM YOU I HAD CLEARLY TOLD YOU 4 NOT MORE!')
      elif count_vowels < 4:
        print(Fore.LIGHTBLUE_EX)
        print('I told you to have atleast 4 vowels in there!')
        print('you should read more carefully!')
      else:
        print(Fore.WHITE)
        print('whaaaat only 4 vowels, realy?? That\'s so boring!')
        print(' Can\'t you be motivated? No congrats for you ... no extra effort niether!')

      
      
      
      
  
  else:
    if decider == 0:
      print()
      print(Fore.RED)
      print('HOW COULD YOU NOT GET SOMETHING THAT EASY RIGHT, YOUR GOING TO GET KICKED OUT OF THE PLANET!!!!! ...')
      print('It dosen\'t even have exactly 8 letters you\'re like a small puddle!!!')
    if decider == 1:
      print()
      print(Fore.RED)
      print('HOW COULD YOU NOT GET SOMETHING THAT EASY RIGHT, YOUR GOING TO GET KICKED OUT OF THE PLANET!!!!! ...')
      print('It dosen\'t even have exactly 7 letters you\'re like a small puddle!!!')
    if decider == 2:
      print()
      print(Fore.RED)
      print('HOW COULD YOU NOT GET SOMETHING THAT EASY RIGHT, YOUR GOING TO GET KICKED OUT OF THE PLANET!!!!! ...')
      print('It dosen\'t even have exactly 9 letters you\'re like a small puddle!!!')
      
  print()
  print(Fore.GREEN + 'Q 3:')
  print()
  print(Fore.WHITE)
  sentence = input('Tell me a sentence that ends with the word "wise assistant" (no questions in answer pleas nor exclamations): ')
  
  if sentence.endswith('wise assistant'):
    print()
    print(Fore.YELLOW)
    print('I think you forgot something ...')
    print('PUNCTATION didin\'t you learn that in school?')
  elif sentence.endswith('wise assistant.'):
    print()
    print('It looks ok to me ... but ... wait ...')
    len_first = sentence.find(' ')
    if len_first < 7:
      print('the first word in you sentence is to short fo me!')
      print('If you don\'t know how to put effort in your work you are a looser!')
    if sentence.startswith(sentence.lower()):
      print('I\'m guessing you didin\'t learn about capital letters.')
  else:
    print()
    print('you didin\'t do what I said so I think you will make the manager very furious!')
    furius = furius + 1
    
  print()
  print(Fore.LIGHTGREEN_EX)
  print('OK')
  print('you did it ok. Not bad!!!')
  print('let\'s see what the manager says about you')
  print('you\'re ready to meet the manager!!!')
  print('you:')
  print(' ____')
  time.sleep(0.5)
  print('|.  .|')
  time.sleep(0.5)
  print('|  o |')
  time.sleep(0.5)
  print(' ----')
  time.sleep(0.5)
  print('(message from manager!)')
  print()
  #appointment slots!
  print(Fore.WHITE)
  print('Ok, please book a slot to meet me on Monday.')
  print()
  print('A. 12 mins past midnight' , 'B. 17 mins before sunrise' , sep = '\t\t')
  print('C. 43 mins before noon' , '    D. 49 mins after eve' , sep = '\t\t')
  print()
  appointment = input('Please choose a booking from the options above (A/B/C/D): ')
  if appointment.lower() == 'a':
    print('Carefull, manager might be asleep.')
  elif appointment.lower() == 'b':
    print('Warning, manger might be getting ready and eating breakfast.')
  elif appointment.lower() == 'c':
    print('Advice, manager might be busy with work.')
  else:
    print('Beware, manager is normaly hanging out with freinds at this time.')
  
  print()
  print('Good luck for your booking, bye for now!!!')
  time.sleep(1)
  if furius == 1:
    print('message from manager:')
    print('My assitant told me you didi\'t do his instructiones so you are fired!')
  ct2 = dt.datetime.now()
  diff = ct2 - ct1
  print()
  print('Wait Whaaaaat you took', diff.seconds, ' seconds to complete such a simple quiz, you are extra slow!')
  print('You think I have no other work ...')
  
if answer == '3':
  ct1 = dt.datetime.now()
  score = 0
  print('the mix of subjects quiz')
  print()
  playrname = input('What is your name?\n')
  print()
  print('This is the profs. office')
  print()
  print('Meet Mr.robot')
  print(Fore.GREEN + 'beep boop IIII aaamm aaa rroobbbbot, nniice ttoo meeeett youuu!')
  print() 
  print('2 questions of english to start')
  print()
  print(Fore.GREEN + 'Q 1:')
  print() 
  time.sleep(1)
  word = input(Fore.WHITE + 'Can you tell me a palindrome word?\n')

  word_p = word[::-1]
  print('Let\'s check')
  print(word_p)

  if word.lower() == word_p.lower():
    print()
    print('OK, you got a palindrome word, but you should have alredy known that since kindergarden!')
    score = score + 1
  else:
    print()
    print('You can\'t even get a palindrome word right, you should go back to school and learn!')
    
  word = input('Now can you tell me a palindrome sentence?\n')

  word_p = word[::-1]
  print('Let\'s check')
  print(word_p)

  if word.lower() == word_p.lower():
    print()
    print('OK, you got a palindrome sentence, but you should have alredy known that since kindergarden!')
    score = score + 1
  else:
    print()
    print('You can\'t even get a palindrome sentence right, you should go back to school and learn!')
  print()
  time.sleep(1)
  print(Fore.GREEN + 'Q 2:')
  print()
  word = input(Fore.WHITE + 'Can you tell me a word with atleast 7 unique letters?\n')

  unique_letters = ''

  for kk in range(len(word)):
    if word[kk] not in unique_letters and (len(unique_letters)) < 7 :
      print('I am going to repeat the same thing')
      print('WHY WON\'T JUST LISTEN TO THE INSTRICTIONES, YOU DID NOT WRIGHT A WORD WITH ATLEAST 7 UNIQUE LETTERS!!!')
      unique_letters = unique_letters + word[kk]
    if word[kk] not in unique_letters and (len(unique_letters)) > 7:
      print('Good, you got it right but there is a lot more to this quiz...')
      
  print('There are', len(unique_letters), 'unique letters in', word)
  print('The unique letters in your word are', unique_letters)
  
  print()
  print('this is to test your IQ')
  print(Fore.GREEN + 'Q 3:')
  print()
  print(Fore.WHITE)
  print('10 * (8/4) + 6 =')
  print()
  print('A. 26' , '    B. 22' , sep = '\t\t')
  print('C. 24.7' , '    D. 20' , sep = '\t\t')
  answer = input('Type down here please:\n')
  if answer.lower() == 'a':
    print(Fore.YELLOW)
    print('It\'s one of those classical and easy ones, so it\'s a relieve you got it right!') 
    score = score + 1
  elif answer.lower() == 'b':
    print(Fore.RED)
    print('It seems like you don\'t even know what maths is...')
  elif answer.lower() == 'c':
    print(Fore.LIGHTYELLOW_EX)
    print('You can see clearly that in the question I have asked you there are no decimales!')
  else:
    print(Fore.LIGHTBLACK_EX)
    print('Not even close')
  print()
  print(Fore.GREEN + 'Q 4:')
  print()
  print(Fore.WHITE)
  answer = input(Style.BRIGHT + Fore.MAGENTA + 'Calculate x. If there are 2 kids and there father gives them each 500$. The first one spends 167$ on a toy robot and x remains. The second one spends 347$ on a toy car and y remains. What is the total remaining?\n')
  print()
  print(Fore.WHITE)
  print(Style.RESET_ALL)
  if answer == '486':
    print(Fore.LIGHTGREEN_EX)
    print('I guess I gave you a such an easy question that even you got it right so I won\'t congrats you or anything.')
    score = score + 1
  else:
    print(Fore.RED)
    print('you are not as smart as I thought you were ...')
    print('I\'m very dissapointed in you ...')
  print()
  print(Fore.GREEN + 'Q 5:')
  print()
  print(Fore.WHITE + 'This is a question of pokemon')
  print()
  answer = input('What is the name of the first pokemon in the pokedex?\n')
  if answer.lower() == 'bulbasaur':
    print('For a pokemon master, that\'s to simple.')
    print('It is number 001 in the pokedex.')
    score = score + 1
  elif answer.lower() == 'pikachu':
    print(Fore.YELLOW)
    print('No way it is Pikacchu, you\'re not even close to becoming a pokemon master.')
    print('Just telling: It is number 025 in the pokedex.')
  else:
    print(Back.RED)
    print('I AM NOT PLEASED WITH YOU!')
    print()
  print(Back.LIGHTBLACK_EX)
  print(Fore.GREEN + 'Q 6:')
  print()
  print(Fore.WHITE)
  print('This is a question of science')
  print()
  answer = input('What is the name of the first element in the periodic table?\n')
  if answer.lower() == 'hydrogen':
    print('Simple, Basic, stuff.')
    score = score + 1
  else:
    print('Don\'t you know the periodic table?')
  print()
  print(Fore.GREEN + 'Q 7:')
  print()
  print(Fore.WHITE)
  print('What would happen if you push something and there was no friction?')
  print()
  
  print('A. It would stop in a few seconds' , 'B. Nothing would happen' , sep = '\t\t')
  print('C. It would keep moving forever' , '    D. It would stop in a few minutes' , sep = '\t\t')
  print('E. It will float' , '                F. It will sink' , sep = '\t\t')
  answer = input('Type down here please:\n')
  if answer.lower() == 'a':
    print('THis is not how science works!')
  elif answer.lower() == 'b':
    print('You are not even close to being a scientist (if you wanted to be one)!')
  elif answer.lower() == 'c':
    print('You got it right, but everyone alredy new thw answer!')
    print('FRICTION obviously!')
    score = score + 1
  elif answer.lower() == 'd':
    print('How would it stop in a few minuits, you are wrong!?')
  elif answer.lower() == 'e':
    print('That\'s gravity, not friction!')
    print('That was not a good answer from you!')
  else:
    print('Think again!')
    print('You thoght you were to smart...')
  print()
  print(Fore.GREEN + 'Q 8:')
  print()
  print(Fore.WHITE)
  print('This is a question of history')
  print()
  answer = input(Fore.YELLOW + 'What year did Columbus discover the Americas?\n')
  print(Fore.WHITE)
  if answer == '1492':
    print('That was the simplest question I could think of!')
    score = score + 1
  elif answer == '1500':
    print('A lot before that!')
  else:
    print('No way, you are wrong!')
  print()
  print(Fore.GREEN + 'Q 9:')
  print()
  print(Fore.WHITE)
  answer = input('Who was the first president of the United States?\n')
  if answer.lower() == 'george washington':
    print('The USA is too famouse, so everyone knows there president!')
    score = score + 1
  elif answer.lower() == 'donald trump':
    print('You are not paying attention to the new and old presidents!')
    print('Donald Trump is the president of now!')
  else:
    print('I think you don\'t even know what president means!')
  print()
  print('final question!!!')
  print()
  print(Fore.GREEN + 'Q 10:')
  print()
  print(Fore.WHITE)
  answer = input('What is the name of the creator of this game?\n')
  if answer.lower() == 'ansh':
    print('Hmmmmm... Oh ya I had forgot my name, but that was just to see you...')
    score = score + 1
  else:
    print('HOW DARE YOU NOT KNOW MY NAME, YOU SHOULD BE ASHAMED OF YOURSELF!')
  print(Fore.BLUE + 'Ring Ring Ring')
  print('It\'s the prof!')
  print()
  print('Nice to meet you', playrname)
  print('Let\'s see your score')
  ct2 = dt.datetime.now()
  diff = ct2 - ct1
  print('You got ' ,score, 'out of 10 in whaaaaaat ' , diff.seconds, 'seconds')
  print('I am disappointed ...')
  print('Now get out of my office!')
  

  

else:
  print('You did not choose a valid option, so please start again and choose a valid option or else...')