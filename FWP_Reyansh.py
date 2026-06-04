import time
import random
import pyfiglet
from colorama import Fore, Style
from os import system
import os
import sys


width = os.get_terminal_size().columns

def clear():
     system("clear")

print(Style.BRIGHT + Fore.LIGHTGREEN_EX + pyfiglet.figlet_format("Login",font="slant", justify="center"))
time.sleep(.8)

for i in range(len("Log in to access your mission information...")):
  print("Log in to access your mission information..."[0:i+1:1], end='\r')
  time.sleep(0.03)
print()
time.sleep(.8)

for i in range(len("Enter Name:")):
  print("Enter Name:"[0:i+1:1], end='\r')
  time.sleep(0.03)
name = input("Enter Name :"+ Fore.BLUE)
time.sleep(.8)

for i in range(len("Password :")):
  print(Fore.LIGHTGREEN_EX+"Password :"[0:i+1:1], end='\r')
  time.sleep(0.03)
input("Password :"+ Fore.BLUE)
print()
time.sleep(.8)

for i in range(len("Conducting voice recognition... Say Hello World")):
  print(Fore.LIGHTGREEN_EX+"Conducting voice recognition... Say Hello World"[0:i+1:1], end='\r')
  time.sleep(0.03)
time.sleep(1.2)
print()
print()
print(Fore.MAGENTA+"               |           |   ".center(width))
print(Fore.MAGENTA+"       |      | |         | |  ".center(width))
print(Fore.MAGENTA+"      | |___|    |       |   | ".center(width))
print(Fore.MAGENTA+"_____|             |____|     |".center(width))
time.sleep(.8)
print()
for i in range(len("Voice verified. Logging in...")):
  print(Fore.LIGHTGREEN_EX+"Voice verified. Logging in..."[0:i+1:1], end='\r')
  time.sleep(0.03)
time.sleep(1.5)

clear()
for i in range(7):
  print()
print(Fore.RED+"--------------".center(width))
print(Fore.RED+"|  --------  |".center(width))
print(Fore.RED+"| |        | |".center(width))
print(Fore.RED+"| |        | |".center(width))
print(Fore.RED+"| |        | |".center(width))
print(Fore.RED+"----------------------------".center(width))
print(Fore.RED+"|                          |".center(width))
print(Fore.RED+"|                          |".center(width))
print(Fore.RED+"|           -----          |".center(width))
print(Fore.RED+"|          |     |         |".center(width))
print(Fore.RED+"|           -   -          |".center(width))
print(Fore.RED+"|            | |           |".center(width))
print(Fore.RED+"|             -            |".center(width))
print(Fore.RED+"|                          |".center(width))
print(Fore.RED+"----------------------------".center(width))
time.sleep(1)

clear()
for i in range(7):
  print()
print(Fore.GREEN+"--------------".center(width))
print(Fore.GREEN+"|  --------  |".center(width))
print(Fore.GREEN+"| |        | |".center(width))
print(Fore.GREEN+"| |        | |".center(width))
print(Fore.GREEN+"| |           ".center(width))
print(Fore.GREEN+"| |           ".center(width))
print(Fore.GREEN+"----------------------------".center(width))
print(Fore.GREEN+"|                          |".center(width))
print(Fore.GREEN+"|                          |".center(width))
print(Fore.GREEN+"|           -----          |".center(width))
print(Fore.GREEN+"|          |     |         |".center(width))
print(Fore.GREEN+"|           -   -          |".center(width))
print(Fore.GREEN+"|            | |           |".center(width))
print(Fore.GREEN+"|             -            |".center(width))
print(Fore.GREEN+"|                          |".center(width))
print(Fore.GREEN+"----------------------------".center(width))

for i in range(3):
  print()

print(Style.BRIGHT + Fore.LIGHTCYAN_EX + pyfiglet.figlet_format("UNLOCKED", justify="center"))
time.sleep(1.8)
clear()

for i in range(len("Access Granted")):
  print(Fore.LIGHTWHITE_EX+ "Access Granted"[0:i+1:1], end='\r')
  time.sleep(0.03)
print()
#(L102) light white lol
time.sleep(1)

for i in range(5):
  print()
number=random.randint(1000,9999)
mission_list= ("you will need to infilitrate the Eiffel Tower because an enemy group is planning to attack France.","you will need to investigate the area around the Great Pyramid of Giza in search of ninjas trying to steal lost artifacts.","you will need to enter the White House undetected, and obtain important data about enemies finding the location of our base.","you will need to find and recruit a notorious hacker and make sure that they are not double crossing us.","you will need to find the mole in our ourginization and track them down." )
mission=random.choice(mission_list)

print(Fore.LIGHTCYAN_EX+"Welcome back, Spy#",number,"aka",name,"! For your mission,",mission,"Good Luck.")

print()
for i in range(len("Press ENTER to continue...")):
  print(Fore.LIGHTGREEN_EX+ "Press ENTER to continue..."[0:i+1:1], end='\r')
  time.sleep(0.03)
  
input(Fore.LIGHTGREEN_EX+"Press ENTER to continue...")
time.sleep(.8)
for i in range(3):
  print()

for i in range(len("This is all classified information it will be deleted in...")):
  print(Fore.LIGHTCYAN_EX+ "This is all classified information it will be deleted in..."[0:i+1:1], end='\r')
  time.sleep(0.03)

time.sleep(1)
print()
print()
print(5)
time.sleep(1)
print()
print(4)
time.sleep(1)
print()
print(3)
time.sleep(1)
print()
print(2)
time.sleep(1)
print()
print(1)
time.sleep(1)
sys.exit()