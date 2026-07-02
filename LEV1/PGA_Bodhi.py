chance = '20%'
chance_n = 20 
fail = 0



print("This is the mr professor professor s assistant")
print("If you want to meet the prof")
print("You have to pass this test")
print("PRESS ENTER TO CONTINUE")
input()
print("What is the answer to life the universe and everything?")
answer = input("\n")
if answer == "42":
   print("you probably googled it didnt you?")
   print("no more of doing that")
   print("ugh...new kids and their phones")
   print("you chance of getting in is ", chance)
else:
  chance_n = chance_n - 10
  chance = str(chance_n) + "%"
  print("idiot")
  print("you probably dont even know what the question is")
  print("a 5 year old with JUST GOOGLE could answer that")
  print("you chance of getting in is " , chance)

print("PRESS ENTER TO CONTINUE")
input("\n")
print()
print("What are action words called?")
answer = input("\n")
if answer.lower() == "verbs":
  chance_n = chance_n + 10
  chance = str(chance_n) + "%"
  print("you probably got that one right by sheer luck")
  print("you chance of getting in is ", chance)

else:
   chance_n = chance_n - 1
   chance = str(chance_n) + "%"
   fail = 1
   print("oh my god")
   print("im dealing with a toodler whose brains have been replaced with a potato")
   print("you chance of getting in is ", chance)
  
print("PRESS ENTER TO CONTINUE")
input()

print("Please give me a 8 letter word with at least 3 vowels")
word = input("\n")
if len(word) == 8:
  print("wow... you know how to count")
  print("im rrreeeaalllyy suprised")
  chance_n = chance_n + 10
  chance = str(chance_n) + "%"

  count_a = word.count("a")
  count_e = word.count("e")
  count_i = word.count("i")
  count_o = word.count("o")
  count_u = word.count("u")

  count_vowels = count_a + count_e + count_i + count_o + count_u

  if count_vowels < 3:
    print("you stupid idiot")
    print("you dont even know what a vowel is")
    if fail == 1:
      print("im sticking to that potato theory")
    print("you chance of getting in is ", chance)  

  elif count_vowels == 3:
    print("exactly three vowels")
    print("the most boring person i have ever met")
    print("you chance of getting in is ", chance)
      
  elif count_vowels > 3:
    #count_vowels > 3
    print("wow what an overachiever")
    print("you probably cry about getting 103% on a test")
    
  
else:
   chance_n = chance_n - 1
   chance = str(chance_n) + "%"
   print("you are a disgrace to humanity")
   print("you chance of getting in is ", chance)

print("PRESS ENTER TO CONTINUE")
input("\n")


print("Please tell me a sentence that starts with _this is_ and ends with _a great assistant_")
print("no questions please and make the thrid word long and put a period after the third word")
sentence = input("\n")
if sentence.startswith("this is"):
  
   if sentence.endswith("a great assistant"):
     
     print("did you NOT PUT A FREAKING PERIOD AT THE END")
     print("you are a disgrace to humanity")
     chance_n = chance_n - 1
     chance = str(chance_n) + "%"
     print("you chance of getting in is ", chance)
     
   elif sentence.endswith("a great assistant."):
     
     print("thanks but flattery wont get you  everywhere in life...idiot")
     len_first = sentence.find(".")
     if len_first <= 7:
       print("you first word is too short")
       print("did you not read the instructions")
       chance_n = chance_n - 1
     print("you chance of getting in is ", chance)

   elif sentence.endswith("not a great assistant."):

     print("you really think im stupid")
     print("you pay for this")
     chance_n = chance_n - 2
     chance = str(chance_n) + "%"

  
     
  
    
   else:
     chance_n = chance_n - 1
     chance = str(chance_n) + "%"
     print("you are a disgrace to humanity")
     print("cant even follow simple instructions")
     
     print("you chance of getting in is ", chance)
     

print("PRESS ENTER TO CONTINUE")
input("\n")

print("that concludes the test")
print("you would have wasted my time")
print("or will now waste the professor's time")
print()
print("You have a", chance, "chance of getting in")
print()
if  chance_n > 5:
  print("by the sheer grace of god you got in")
  print("now choose your appointment time")
  print("A - Morning")
  print("B - Afternoon")
  print("C - Evening")
  print("D - Night")
  answer = input("\n")
  
  if answer == "A":
    print("you will be meeting the professor at 9:00 AM")
  elif answer == "B":
    print("you will be meeting the professor at 1:00 PM")
  elif answer == "C":
    print("you will be meeting the professor at 5:00 PM")
  elif answer == "D":
    print("you will be meeting the professor at 9:00 PM")
  elif answer == "E":
    print("oh my god")
    print("have you lost your mind")
    print("you DIDNT EVEN READ THE FREAKING QUESTIONS")
    print("you will not be meeting the professor")
  print("now...can you please go away")
  
else:
   print("you did soo bad on the test")
   if fail == 1:
    print("mr prof is not gonna meet THE FREAKING POTATO")
   else:
     print("you will not be meeting the professor")

print("THANKS FOR PLAYING")
print("PLS DONT TAKE THIS TOO SERIOUSLY")
print("SEE YOU NEXT TIME")
print("100000000000000000000000% me")
