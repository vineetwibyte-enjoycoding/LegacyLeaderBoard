import tkinter as tk
import random  #imports

#opening 5 Letter word file (reading and closing it too) as a large string
f = open("5L words.txt")
words = f.read()
#making that string into a list
WordList = words.split("\n")
f.close()

guess_no = 0
#a boolean variable used to make sure to prevent an error while deleting
#widgets(in this case, the widgets related to the hint)
IsHint = False

#I have used 4 functions in my project: guess(), Hint(), entry() and GIVE_UP().


#a function that is called when the user clicks the check button to confirm word guess
def guess():

  count = 0
  global guess_no
  global GuessedWord

  #check of validity of word in terms of it is 5 letters long or is an actual word
  GuessedWord = entry_guess.get()
  if len(GuessedWord) > 5:
    #too long
    print("The word is too long")
  elif len(GuessedWord) < 5:
    #too short
    print("The word is too short")
  else:
    #is not the in the word list(not valid)
    if GuessedWord.lower() not in WordList:
      print("The word is not valid")
    else:
      #adding each letter guessed to the mainscreen
      for kk in range(5):
        label_guess = tk.Label(
            text=GuessedWord[kk].upper(),
            bg="white",
            fg="black",
            font=("Bahnschrift", 28, "bold"),
            relief="raised",
            anchor="center",
            width=1,
            padx=22,
        )
        #writing the word on the mainscreen
        label_guess.grid(row=guess_no, column=kk, sticky=tk.NSEW)
        #check if the letter is in the right place
        if GuessedWord[kk].lower() == ChosenWord[kk]:
          label_guess.configure(bg="ForestGreen")
        elif GuessedWord[kk].lower() in ChosenWord:
          label_guess.configure(bg="Gold")
          # repitition of letter check(as given in video)
          Occurences = GuessedWord.count(GuessedWord[kk]) - ChosenWord.count(
              GuessedWord[kk])
          if count < Occurences:
            label_guess.configure(bg="DarkGrey")
            count += 1
        else:
          label_guess.configure(bg="DarkGrey")
          #winning condition
        if GuessedWord.lower() == ChosenWord and guess_no < 6:
          #if hint has been opened(check to prevent error)
          if IsHint is not False:
            Label.config(text="!  WON in {} guesses  !".format(guess_no + 1))
            Label.place(x=103, y=295)
            Check.destroy()
            entry_guess.destroy()
            Hint_Button.destroy()
            Hint_no_L.destroy()
            Hint_no_E.destroy()
            Check1.destroy()
            Give_up.destroy()
            window.geometry("405x400")
            #if hint is not opened
          else:
            Label.config(text="!  WON in {} guesses  !".format(guess_no + 1))
            Label.place(x=103, y=295)
            Check.destroy()
            entry_guess.destroy()
            Hint_Button.destroy()
            Give_up.destroy()
            window.geometry("405x400")

        #losing condition
        if guess_no == 5 and GuessedWord.lower() != ChosenWord:
          #if hint has been opened(check to prevent error)
          if IsHint is not False:
            Label.config(text="!  GAME LOST  !\nThe word was {}".format(
                ChosenWord.upper()))
            Label.place(x=103, y=295)
            Check.destroy()
            entry_guess.destroy()
            Hint_Button.destroy()
            Hint_no_L.destroy()
            Hint_no_E.destroy()
            Check1.destroy()
            Give_up.destroy()
            window.geometry("405x400")
          else:
            #if hint is not opened
            Label.config(text="!  GAME LOST  !\nThe word was {}".format(
                ChosenWord.upper()))
            Label.place(x=103, y=295)
            Check.destroy()
            entry_guess.destroy()
            Hint_Button.destroy()
            Give_up.destroy()
            window.geometry("405x400")

      #increasing guess_no
      guess_no += 1
      if GuessedWord.lower() != ChosenWord:
        deleted = entry_guess
        del deleted


#Hint boutton has been clicked
def Hint():
  x = 380
  y = 180
  #finding the number of the desired position given by user
  pos = Hint_no_E.get()
  POSITON_of_hint = int(pos)
  #the letter the user wants to know
  Hint_pos = ChosenWord[POSITON_of_hint - 1]
  #revealing the letter and adding _ in the other spaces
  #adding the letter
  for kk in range(5):
    if kk + 1 == POSITON_of_hint:
      label_hint = tk.Label(text=Hint_pos.upper(),
                            bg="white",
                            fg="black",
                            font=("Bahnschrift", 20, "bold"))
      label_hint.place(x=x, y=y)
      x += 25
      #and adding the underscores
    else:
      label_hint = tk.Label(text="_",
                            bg="white",
                            fg="black",
                            font=("Bahnschrift", 20, "bold"))
      label_hint.place(x=x, y=y)
      x += 25

  #destroying the hint related widgets to prevent repeated hints given
  Hint_no_L.destroy()
  Hint_no_E.destroy()
  Hint_Button.destroy()
  Check1.destroy()


#making the hint related widgets
def entry():
  global Hint_no_E
  global Hint_no_L
  global Check1
  global IsHint
  #Hint has been clicked(why I have added this variable is given in line 12 and 13)
  IsHint = True
  #label for hint
  Hint_no_L = tk.Label(text="Type the position \nno. of the letter",
                       font=("Bahnschrift", 10, "bold"))
  Hint_no_L.place(x=367, y=85)
  #entry box for hint
  Hint_no_E = tk.Entry(window)
  Hint_no_E.configure(justify="center",
                      font=("Bahnschrift", 10, "bold"),
                      width=6,
                      bg="white",
                      fg="black",
                      borderwidth=3,
                      relief="raised",
                      highlightthickness=2,
                      highlightbackground="black",
                      highlightcolor="black",
                      selectbackground="black",
                      selectforeground="white",
                      insertbackground="black",
                      insertwidth=2,
                      state="normal")
  Hint_no_E.place(x=390, y=135)

  #the check button to confirm the desired position in word
  Check1 = tk.Button(window,
                     text="✔",
                     bg="white",
                     fg="black",
                     font=("Bahnschrift", 10, "bold"),
                     command=Hint)
  Check1.place(x=460, y=134)


#the give up button
def GIVE_UP():
  #if hint has been opened(check to prevent error)
  if IsHint is not False:
    Label.config(
        text="!  GAME LOST  !\nThe word was {}".format(ChosenWord.upper()))
    Label.place(x=103, y=295)
    Check.destroy()
    entry_guess.destroy()
    Hint_Button.destroy()
    Hint_no_L.destroy()
    Hint_no_E.destroy()
    Check1.destroy()
    Give_up.destroy()
    window.geometry("405x400")
    #if hint is not opened
  else:
    Label.config(
        text="!  GAME LOST  !\nThe word was {}".format(ChosenWord.upper()))
    Label.place(x=103, y=295)
    Check.destroy()
    entry_guess.destroy()
    Hint_Button.destroy()
    Give_up.destroy()
    window.geometry("405x400")


#getting the chosen word
ChosenWord = random.choice(WordList)
print(ChosenWord)

#setting up the window
window = tk.Tk()
window.title("Wordle")
window.geometry("545x400")
window.configure(bg="white",
                 padx=10,
                 pady=10,
                 borderwidth=5,
                 relief="raised",
                 highlightthickness=5,
                 highlightbackground="black",
                 highlightcolor="black")
window.resizable(False, False)

#addin the hint button
Hint_Button = tk.Button(text="HINT",
                        font=("Bahnschrift", 20, "bold"),
                        command=entry)
Hint_Button.place(x=385, y=30)

#the entry box for the mainscreen
entry_guess = tk.Entry(window)
entry_guess.configure(justify="center",
                      font=("Bahnschrift", 10, "bold"),
                      width=30,
                      bg="white",
                      fg="black",
                      borderwidth=3,
                      relief="raised",
                      highlightthickness=2,
                      highlightbackground="black",
                      highlightcolor="black",
                      selectbackground="black",
                      selectforeground="white",
                      insertbackground="black",
                      insertwidth=2,
                      state="normal")
entry_guess.place(x=20, y=305)

#setting up the intial template for the mainscreen on which the guessed word will
#be written(the grey blocks at the start)
for jj in range(6):
  for kk in range(5):
    label_guess = tk.Label(text="".upper(),
                           bg="Silver",
                           fg="black",
                           font=("Bahnschrift", 28, "bold"),
                           relief="raised",
                           anchor="center",
                           width=1,
                           padx=22)
    label_guess.grid(row=jj, column=kk, sticky=tk.NSEW)

#label for the mainscreen
Label = tk.Label(window,
                 text="Guess the word",
                 bg="white",
                 fg="black",
                 font=("Bahnschrift", 10, "bold"))
Label.place(x=104, y=340)

#the check button to confirm the word
Check = tk.Button(window,
                  text="✔",
                  bg="white",
                  fg="black",
                  font=("Bahnschrift", 10, "bold"),
                  command=guess)
Check.place(x=307, y=304)

#the give up button
Give_up = tk.Button(text="Give up?",
                    font=("Bahnschrift", 10, "bold"),
                    bg="white",
                    fg="black",
                    command=GIVE_UP)
Give_up.place(x=395, y=300)

#I am not sure if this is necessary
window.mainloop()
#mainloop
tk.mainloop()

#at the end it was a lot of fun to make this project. It was really hard too
#because I had to make a lot of changes to the code to make it work. I had many
#errors like wrong indentation, wrong variable names, etc. But overall an amazing
#experience for me. Thank you VINEET SIR for all the knowledge on coding i have now
