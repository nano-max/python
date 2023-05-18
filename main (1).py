# casting -- explicitly define that the input is a number and not a letter

print("=======GENERATION GENERATOR==========")
print("""What generation are you part of?
Are you a traditionalist? Or a Baby Boomer? Or are you a Generation X, Y, or Z? What are the differences between all of these anyways?
Interested to learn more? Then answer the next questions, and we'll tell you!

""")
year=int(input("In which year were you born?"))
if year < 1925:
  print("Man, you're an OG. I have no official generation name for you, you're just a real OG in my eyes. Respect.")
elif year >=1925 and year <= 1946:
  print("Nice, that's a respectable age. You're a Traditionalist!")
elif year >=1947 and year <=1964:
  print("You're still in the prime of your life, Baby Boomer!")
elif year >=1965 and year <=1981:
  print("Yay - you belong to Generation X.")
elif year >=1982 and year <=1995:
  print("You belong to the awesome Millenials. The sky is the limit!")
elif year >= 1996 and year <=2015:
  print("Hey, Generation Z -- you can do anything in life. Live freely!")
else:
  print("Darn - you're young.")