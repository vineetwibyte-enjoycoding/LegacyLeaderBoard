print(' Welcome to the prof\'s office')
print('So you want to meet the prof')
print('But first, you have to pass my quiz')
print()
import time
time.sleep(1.5)
#First bonus - determining how long the user took to respond
import datetime as dt

ct1 = dt.datetime.now()
word = input('Tell me a sentence with 11 words. \n')
ct2 = dt.datetime.now()
diff = ct2-ct1
print('What ...', diff.seconds, 'seconds to answer that ..... even my uneducated ancestors who worked as coolies could do better')
# second question
answer = input('ok, what are action words called in english\n')
#Second bonus- Removing trailing and leading spaces from the user response using the strip() method
answer_s = answer.strip()

if answer_s.lower() == 'verbs':
  print('Correct, but that was just a warmup')
else:
  print('A failure meeting the prof, I have my reservations about that')
#Third Bonus-Determining how much unique letters there are in a word
print()
word = input('Tell me a word with lots of unique letters\n')


unique_letters = ''

for kk in range(len(word)):
  if word[kk] not in unique_letters:
    unique_letters = unique_letters + word[kk]
  

print(unique_letters)
print('What! only',(len(unique_letters)),'unique letters, can you do any better?')
print('Useless!')


#Third question
print()
print()
print()
print()
print()
word = input('ok, tell me an english word with 8 letters and at least 3 vowels\n')
#checks if the word meets the requirements
#⬇️⬇️⬇️⬇️⬇️nested loop!⬇️⬇️⬇️⬇️⬇️
if len(word) == 8:
  print('Ok, your word has 8 letters')
  count_a = word.count('a')
  count_e = word.count('e')
  count_i = word.count('i')
  count_o = word.count('o')
  count_u = word.count('u')
  count_vowels = count_a + count_e + count_i + count_o + count_u
  if count_vowels>3:  
    print('Ooff ... you gave me more than 3 vowels')
    print('You are wasting my time ... I needed only 3')
  elif count_vowels<3:
    print('That has less than 3 vowels...')
    print('You tried acting smart, but I caught you') 
  else:
    print('What ... exactly 3 vowels!?')
    print('You are not motivated at all')
else:
  print(' You seem to be a tragedy')
  print ('That did not even have 8 letters')

sentence = input('ok, tell me a sentence ending in wise assistant (no qns please)\n')

if sentence.endswith('wise assistant'):
  print('Haven\'t you learnt about punctuations?')
elif sentence.endswith('wise assistant.'):
  print('your sentence seems ok ...')
  len_first = sentence.find('')
  if len_first < 8:
   print('Your first word was too small')
  else: 
   print('sentence looks fine, but your standards are very low')
else:
  print('Spectualation confirmed: You are a failure')
#Appointment time
print()   
print("Ok, pick your preferred appointment time for next Friday(A/B/C/D)")
print("A. 16:48", "B. 6:00", sep='\t') 
print("C. 11:23", "D. 19:48", sep='\t')
appointment = input('Select your slot (A/B/C/D)\n')

if appointment == 'A':
    print("Careful! Prof may be half-dead from work!")
elif appointment == 'B':
    print("Warning! Prof may be doing morning exercise!")
elif appointment == 'C':
    print("Beware! Prof may be busy with work!")
else:
    print("Caution! Prof may be eating dinner!")

print()
print("Good luck for your appointment! We shall bid farewell for now!")