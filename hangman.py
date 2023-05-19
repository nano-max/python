import random, os, time
listOfGuesses=[]
solution=[]
unguessed=[]
won=[]

listOfWords = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

myWord=random.choice(listOfWords).lower()
unguessedI=myWord

print()

for i in range(0,len(myWord)):
  solution.append("_")
  
def printResult():
  i=6-lives
  print("\033[33m",HANGMANPICS[i],"\033[0m")
  print("\n")
  for underscore in solution:
    print(f"{underscore}",end="")
  print("\n")

for character in unguessedI:
  unguessed.append(character)

for m in range(0,len(myWord)):
  won.append("")

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives=6

while True:
  time.sleep(1.5)
  os.system("clear")
  print("======== HANGMAN ========")
  print()
  printResult()
  if lives>0:
    if unguessed!=won:
      guess=input("\nChoose a letter: ").lower()
      if guess in listOfGuesses:
        print("\033[31m","You've already tried that before. Choose another one.","\033[0m")
      else:
        if guess in myWord:
          print("\033[32m","Correct!","\033[0m")
          listOfGuesses.append(guess)
          position=0
          for letter in unguessed:
            if letter==guess:
              solution[position]=guess
              unguessed[position]=""
              position+=1
            else:
              position+=1
        else:
          print("\033[31m","Nope, not in there")
          print(f"{lives-1} lives left.","\033[0m")
          listOfGuesses.append(guess)
          lives-=1
    else:
      print("\033[32m","🎉 Congrats!")
      print(f"You've won with {lives} lives left!")
      break
  else:
    print("\033[31m",f"😢 You have no lives left. You lost! The right answer was '{myWord}'.")
    break
  
    