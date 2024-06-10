name1 = input("Enter your full name: ")
name2 = input("Enter your full name: ")

combined_names = (name1.lower() + " " + name2.lower())

has_true = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')

has_love = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

love_score = str(has_true) + str(has_love)
score = int(love_score)

if (score < 10) or (score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
