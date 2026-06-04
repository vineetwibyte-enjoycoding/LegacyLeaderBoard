import colorama
import time
from colorama import Fore, Back, Style
import pyfiglet

hw="Hello world"
py1=pyfiglet.figlet_format(hw, font='slant')
print(py1)


#statement a  animation
print()
print(Fore.CYAN)
welcome_message = "Welcome to the survey"
for a in range(len(welcome_message) + 1):
    print(welcome_message[0:a], end= '\r')
    time.sleep(0.1)
print()
#statement a over

#statement b animation
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX)
messageb ="First you will have to put some details about yourself"
for b in range(len(messageb) + 1):
  print(messageb[0:b], end= '\r')
  time.sleep(0.1)
print('First you will have to put some details about yourself')
#statement b over

#statement c
print()
print(Fore.YELLOW)
messagec ="Would you like to continue "
for c in range(len(messagec) + 1):
  print(messagec[0:c], end= '\r')
  time.sleep(0.1)
ans=input("Would you like to continue \nAnswer yes or no \n")
#statement c over
if ans== 'no':
    print('Bye')
else:
  print(Fore.LIGHTGREEN_EX)
  print('Great then!')
print('Please wait')

time.sleep(2) 
print(Back.RED)
name=input("May we know your name ?\n" )
#trying to add a while loop
while name=="":
  print('No name entered')
  name=input("May we know your name ?\n")
print(Back.LIGHTYELLOW_EX)
print("Hello",name)

# A space will be detected
# Trying to add a space in the name
surname=input("May we know you last name?\n (Optional)\n")
print(Back.RESET)
print(Fore.BLUE)
#age
age = input("How old are you?\n")
# Trying to add a space in the age
while age=="" :
  print('No age entered')
  age=input("How old are you?\n")
print(Fore.LIGHTGREEN_EX)
if int(age)<18:
   print("Sorry you can not continue this survey as you are under 18")
else:
  print("Please wait")
time.sleep(3)
print(Fore.LIGHTRED_EX)
birthyear = input('Please enter your birth year')
while 2023-int(birthyear)!= int(age):
  print("You have entered the wrong birth year")
  birthyear = input('Please enter your birth year')

print(Fore.LIGHTCYAN_EX)
#email
email=input("please put your valid email address")
while email=="":
  print("No email entered")
  email=input("please put your valid email address")
time.sleep(1)
print(Fore.MAGENTA)
#final information
print("Now we have all your details please check if your details are correct ")
time.sleep(1)
print("if not please resubmit the form from begainning")
time.sleep(1)
print("Name:",name,surname)
time.sleep(1)
print("Age:",age)
time.sleep(1)
print("Birth year:",birthyear)
time.sleep(1)
print("Email address:", email)
time.sleep(1)
check=input("Are your details correct")
if check =='yes':
  print("Okay")
else:
  print("Please resubmit the form from begainning")
time.sleep(1.5)
print(Fore.LIGHTBLUE_EX)
print("WELCOME TO ")
print("PPPPP Y    Y TTTTT H   H OOOOO N   N")
print("P   P  Y  Y    T   H   H O   O NN  N")
print("PPPPP   Y      T   HHHHH O   O N N N")
print("P       Y      T   H   H O   O N  NN") 
print("P       Y      T   H   H OOOOO N   N")    
print()
time.sleep(3)
print("We will just",Fore. GREEN, "confirm if you", Fore.MAGENTA,"are not a",Fore.RED)
s='R O B O T'
time.sleep(1)
sur=pyfiglet.figlet_format(s, font='3-d')
print(sur)
time.sleep(2)
a100=input("Add 100 to your age and enter here")
if int(a100)==int(age)+100:
  print("")
  print('You will be able to login in a few hours now ')
  print("We will notify you as soon as we get your account")
  ty='THANK YOU '
  ty1=pyfiglet.figlet_format(ty, font='bulbhead')
  print(ty1)
else:
  print("You have entered the wrong number")





      

