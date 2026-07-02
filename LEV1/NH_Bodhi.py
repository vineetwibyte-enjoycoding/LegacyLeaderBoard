import random 

print("WELCOME TO THE TV SHOW!!!!")
print("GUEES THAT NUMBERR\n")

n = random.randint(1, 100)
chance = random.randint(1, 10)
print("The number is between 1 and 100\n")
print("You have 25 guesses\n")
if n % 2 == 0:
  print("The number is even\n")
else:
  print("The number is odd\n")
if chance == 10:
  if len(str(n)) == 2:  
    print("The digits add up to", n % 10 + n // 10) 

atempmt = 0
done = False


while not done:
  guess = int(input("Guess a number\n")) 
  if guess > 100 or guess < 1:
     print("Wrong input")
  else:
     if guess > n:
       print("THE NUMBER IS LOWER")
     if guess < n:
       print("THE NUMBER IS HIGHER")
     if guess == n:
       print("YOU WIN")
       print("You had", 25 - atempmt, "guesses left")
       done = True  
     if atempmt > 25:
        print("YOU LOSE")
        done = True
        print("The number was", n)
     atempmt = atempmt + 1

print()
print()
print()
print("NOW ITS TIME FOR THE NEXT ROUND")
print("ITS YOUR TURN NOW")
print("PICK A NUMBER IN YOUR HEAD")
print("I WILL GUESS IT")
print("PRESS ENTER TO CONTINUE")
input()
print("OKAY BEFORE WE START\n")
print("HERE ARE THE RULES")
print("y = yes so if i guess the number right you say y\n" )
print("h = higher so if the number is higher than my guess you say h\n")
print("s = smaller so if the number is lower than my guess you say s\n")
print("PRESS ENTER TO CONTINUE")

input()

done = False
atempmt = 0
guess = 1
guess_step = 10
prev_answer = ''

while not done:
  answer = input("Is your number " +  str(guess) + " ?\n")

  if atempmt > 1:
    if prev_answer != answer :
      guess_step = guess_step - 1

  prev_answer = answer
  
  atempmt = atempmt  + 1

  if answer  == "h":
    guess = guess + guess_step
    if guess > 100:
      guess = 100
  if answer == "s":
    guess = guess - guess_step
    if guess < 1:
      guess = 1
  if answer == "y":
   print("I WIN")
   print("I took", atempmt, "guesses")
   done = True

print("NOW TIME FOR THE FINAL ROUND\n")
print("ILL BE SMARTER THIS TIME")
print("AHAHAHAHHAHAHAHAHAHHAHAHAHAHHAHAHAHHA")
print("PRESS ENTER TO CONTINUE")
input("\n")
print("Same rules as BEFORE")
print("PRESS ENTER TO CONTINUE")
input()

done = False
atempmt = 0
guess = 1
high = 100
low = 1

while not done:

  guess = round((high + low) / 2)
  answer = input("Is your number " +  str(guess) + " ?\n")


  atempmt = atempmt  + 1

  if answer  == "h":
    low = guess
  if answer == "s":
    high = guess
  if answer == "y":
    print("I WIN")
    print("I took", atempmt, "guesses")
    done = True


