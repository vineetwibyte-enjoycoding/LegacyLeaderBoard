import random
import time
discard=[]
#smallestnum=2



cards=["2","3","3","4","5","6","7","8","9","10","J","Q","K","A"]
suits=["C","D","H","S"]
deck=[]

smallestnum=cards[0]

def cleanup(smallestnym):
  for c in tablecards:
    if c[1]==smallestnym:
      tablecards.remove(c)
      discard.append(c)






for jj in range(len(suits)):
  for kk in range(len(cards)):
    deck.append(suits[jj]+cards[kk])

for kk in range(len(deck)):
  print(deck[kk],end=" ")

print()
print()
random.shuffle(deck)
#for kk in range(len(deck)):
  #print(deck[kk],end=" ") 
tablecards=[]
toss=random.choice(deck)
if toss[0]=="C"or toss[0]=="S":
  first="player"
  print("you win, you play first")
else:
  first="computer"
  print("comuter wins it plays first")

playerc=deck[:26:]
computerc=deck[26::]


gamecomp=False
movecomp=False
moves=0
while not gamecomp:
  movecomp=False
  tablecards.clear()
  if len(playerc)<3 or len(computerc)<3:
    movecomp=True
    gamecomp=True
  while not movecomp:
    choice=False
    while not choice:
      print("Choose from these three cards",end=" ")
      card_p=input(playerc[0]+","+playerc[1]+"," + playerc[2]+"\n")
      if card_p in playerc[:3:1]:
        choice=True
        playerc.remove(card_p)
      
    if moves>10:
      movecomp=True
      gamecomp=True
    
    card_c=computerc.pop(0)
    print("player card is ",card_p)
    print("computer card is ",card_c)
    tablecards.append(card_p)
    tablecards.append(card_c)
    if cards.index(card_p[1::])>cards.index(card_c[1::]):
      print(tablecards,discard)
      print("player wins")
      time.sleep(1)
      playerc.extend(tablecards)
      cleanup(smallestnum)
      tablecards.clear()
      movecomp=True
      moves=moves+1
      if len(discard)/4==cards.index(smallestnum)+1:
        smallestnum=cards[cards.index(smallestnum)+1]
    elif cards.index(card_p[1::])<cards.index(card_c[1::]):
      print(tablecards,discard)
      print("computer wins")
      time.sleep(1)
      cleanup(smallestnum)
      computerc.extend(tablecards)
      tablecards.clear()
      movecomp=True
      moves=moves+1
      if len(discard)/4==cards.index(smallestnum)+1:
        smallestnum=cards[cards.index(smallestnum)+1]
    else:
      print("War begins...")
      if len(playerc)<4 or len(computerc)<4:
        movecomp=True
        gamecomp=True
      else:
        tablecards.extend(playerc[::3])
        tablecards.extend(computerc[::3])
        del(playerc[:3:])
        del(computerc[:3:])
        


if len(playerc)>len(computerc):
  print("player wins................")
elif len(playerc)<len(computerc):
  print('computer wins..............')
else:
  print("game drawn")
  