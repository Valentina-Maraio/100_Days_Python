# Condition
greetings = "Welcome to the rollercoaster!"
print(greetings)

height = int(input("What is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    bill = 0
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif 12 < age < 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
        """ elif 45 < age < 55:
        bill = 0
        print(f"Your tickets are ${bill}") """
    elif age >= 45 and age <= 55:
        print("You ride for free!")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")
    photo = input("A photo would cost $3. Do you want a photo? Y or N ")
    if photo == 'Y':
        bill += 3
        print(f"So your total is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Greater than >
# Less than <
# >= Greater than or equal to
# <= Less than or equal to.
# Equal to ==
# Not equal to !=

number = int(input("Give me a number and I'll tell you if it is odd or even.\n"))

if number % 2 == 0:
  print(f"{number} is an odd number.")
else:
  print(f"{number} is an even number.")

# Nested if / else statement
