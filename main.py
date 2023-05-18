print("=============LOTR QUIZ================")
print()
print("""This is your favorite LOTR quiz. Which of the races on the Middle Earth do you belong to?
Let's find out!

Answer the next questions as accurately and honestly as you can.""")
print()
nature = input("Do you like to live with nature? Y/N:")
if nature == "Y":
  sleepLocation = input("Would you rather sleep at great heights or under the ground? :")
  if sleepLocation == "great heights":
      print("Yay, you should live with the", "\033[33m", "elves","\033[0m", "in Middle Earth! I'm sure you'll enjoy it.")
  else:
      print("Yes, I agree that under the ground is much more comfortable. You should stay with the","\033[32m","Hobbits","\033[0m","in Middle Earth. They are a merry bunch.")
else:
  light=input("Gotcha, let's stay in cities then. Would you rather live under the direct sunlight, or in a place that is lighted with magic lamps?")
  if light=="magic lamps":
    print("Yay, I agree magic is interesting. You should try stay with the","\033[37m","dwarves","\033[0m","in the glittering caves. I guarantee that you'll love it.")
  else:
    print("That makes sense. You would totally fit in with the","\033[34m","humans","\033[0m","on Middle Earth. They build magnificent cities.")
print()
print("Hope you liked this little quiz, one does not simply choose a race!")
