import tkinter as tk



def pressnum(num):
  text=entr.cget('text')
  entr.configure(text=text+str(num))

def pressop(op):
  text=entr.cget('text')
  txt2=expr.cget('text')
  expr.configure(text=txt2+text+op)
  entr.config(text='')

def C():
  entr.configure(text="")
  expr.configure(text='')

def presseq():
  textentr=entr.cget("text")
  textexpr=expr.cget("text")
  expr.configure(text=textexpr+textentr+'=')
  result=eval(textexpr+textentr)
  entr.configure(text=str(result))
  
  


window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")

expr=tk.Label(window,text='',bg='black',fg='white',width=45,height=4,borderwidth=3,relief=tk.RIDGE,anchor=tk.E)
expr.grid(row=0,column=0,columnspan=4)
entr=tk.Label(window,text='',bg='black',fg='white',width=46,height=5,borderwidth=3,relief=tk.RIDGE,anchor=tk.E)
entr.grid(row=1,column=0,columnspan=4)

brow=3
bcol=0

numlist = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['x', 'x', '.']
]

for kk in range(len(numlist)):
  for jj in range(len(numlist[0])):
    if numlist[kk][jj].strip() != 'x':
      tk.Button(text=numlist[kk][jj],bg='black',fg='white',command=lambda x=kk,y=jj:pressnum(numlist[x][y].strip())).grid(row=kk+brow,column=jj+bcol,sticky=tk.NSEW)
    
      
br=2
bc=0
oplist=['/','*','+','-']

for kk in range(len(oplist)):
  tk.Button(
      text=oplist[kk],
      bg='black',
      fg='white',
      command=lambda x=kk: pressop(oplist[x])
  ).grid(row=br, column=kk+bc,sticky=tk.NSEW)

#tk.Button(text='/',bg='black',fg='white',command=lambda:pressop('/')).grid(row=2,column=3,sticky=tk.NSEW)
tk.Button(text='C',bg='black',fg='white',command=lambda:C()).grid(row=3,column=3,rowspan=2,sticky=tk.NSEW)


#tk.Button(text='x',bg='black',fg='white',command=lambda:pressop('*')).grid(row=3,column=3,sticky=tk.NSEW)


#tk.Button(text='-',bg='black',fg='white',command=lambda:pressop('-')).grid(row=4,column=3,sticky=tk.NSEW)
tk.Button(text='=',bg='black',fg='white',command=lambda:presseq()).grid(row=5,column=3,rowspan=2,sticky=tk.NSEW)

tk.Button(text='0',bg='black',fg='white',command=lambda:pressnum(0)).grid(row=6,column=0,columnspan=3,sticky=tk.NSEW)

#tk.Button(text='+',bg='black',fg='white',command=lambda:pressop('+')).grid(row=5,column=3,sticky=tk.NSEW)

tk.mainloop()