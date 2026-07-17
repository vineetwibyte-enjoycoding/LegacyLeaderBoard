import tkinter as tk
import random

def hint():
	hintbutton.config(text = 'First letter: '+chosenword[0]+ ', last letter: '+chosenword[5])
	
guessnum = 0

def getword():
	guessedword = entrybox.get()
	global guessnum
	cnt = 0
	if guessnum < 7:
		if guessedword in wordlist:
			for i in range(6):
				label = tk.Label(text = guessedword[i].upper(), pady = 7, padx = 7, font = ('Times New Roman', 12), width = 2, borderwidth = 1, relief = 'groove')
				label.grid(row = guessnum, column = i, sticky = tk.NSEW)
				if guessedword[i] in chosenword:
					if guessedword[i] == chosenword[i]: 
						label.config(bg = 'forestgreen')
						label.config(fg = 'white')
					else:
						label.config(bg = 'goldenrod')
						label.config(fg = 'white')
						if cnt < guessedword.count(guessedword[i]) - chosenword.count(guessedword[i]):
							label.config(bg = 'dimgrey')
							label.config(fg = 'white')
							cnt = cnt + 1
				else:
					label.config(bg = 'dimgrey')
					label.config(fg = 'white') 
		else:
			print('Invalid word, please try again')
		#guessnum = guessnum + 1

		if guessnum == 7:
			guessbutton.config(text = 'Maximum Guesses Reached', font = ('Times New Roman', 9))
			word = tk.Label(text = 'The word was ' + chosenword, font = ('Times New Roman', 9))
			word.grid(row = 101, column = 0, columnspan = 6)

	else:
		guessbutton.config(text = 'Maximum Guesses Reached', font = ('Times New Roman', 9))
		word = tk.Label(text = 'The word was ' + chosenword, font = ('Times New Roman', 9))
		word.grid(row = 101, column = 0, columnspan = 6)
	guessnum = guessnum + 1

window = tk.Tk()
window.title("6-letter wordle")
window.geometry("250x400")

f = open('SixLetter_Alphabetic.txt')
words = f.read()
f.close()
wordlist = words.split('\n')
chosenword = random.choice(wordlist)


entrybox = tk.Entry()
entrybox.grid(row = 99, column = 0, columnspan = 6)

guessbutton = tk.Button(text = 'Guess Word', font = ('Times New Roman',9),command = getword)
guessbutton.grid(row = 100, column = 0, columnspan = 6)

hintbutton = tk.Button(text = 'HINT',font = ('Times New Roman',9),command = hint)
hintbutton.grid(row = 103, column = 0, columnspan = 6)