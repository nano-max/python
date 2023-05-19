# getpass - hide input when typing

from getpass import getpass as input
print("===========ROCK, PAPER, SCISSORS - CHAMPIONSHIP==========")
print("""And WELCOME!! To the most popular game -- rock, paper, scissors!

You can play this game with 2 players.

""")
player1=input("Name of player 1: ")
player2=input("Name of player 2: ")
print()
print("Hey, ",player1,"!")
inputP1=input("Do you choose for rock (R), paper (P), or scissor (S)? : ")
print("Hey",player2,"!")
inputP2=input("How about you? Do you choose for rock (R), paper (P), or scissor (S)? : ")
print()
print("""...
Thank you both. Now comes the result...
...
Who will win?
Who is the better of the two of you??? (Jk)
...
🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁🥁

""")
if inputP1=="S" and inputP2=="P":
  print("congrats,",player1,"you've won!")
elif inputP1=="P" and inputP2=="R":
  print("congrats,",player1,"you've won!")
elif inputP1=="R" and inputP2=="S":
  print("congrats,",player1,"you've won!")
elif inputP1==inputP2:
  print("It's a tie!")
else:
  print("Congrats",player2,", you've won!")