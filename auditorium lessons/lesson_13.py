# Randomisation and Python Lists
# Sudo random number generator
# Python uses Mersenne Twister
# Data Structure Page: https://docs.python.org/3/tutorial/datastructures.html

import random
from your_modules import pi_module

random_int = random.randint(1, 10)
# random int
print(f"random integer: {random_int}")

random_float = random.random() * 5

# random float

print(f"random float number: {random_float}")

print(f"Pi value from imported module: {pi_module.pi}")

print(f"Name value imported from module: {pi_module.name}")

# a module is a part of the code

print("\nLESSON 13 - CHALLENGE\n")

# Toss a virtual coin and get a random result.

Heads = 1
Tails = 0

toss = random.randint(0, 1)

if toss == 1:
    print("Heads")
else:
    print("Tails")

# THE LIST. List is a data structure. A way of organizing and storing data in python.
magic_words = ['banana', 'fish', 'gorilla', 'shoelace']

print(magic_words)

# I want to store all the names of the US states.
usa_states_name = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina",
    "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
    "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
    "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
]

# print a state from a specific index
print(usa_states_name[7])  # South Carolina

# change the value of an item in the list.
usa_states_name[8] = "!!!VALENTINA!!!"
print(usa_states_name)  # 'Maryland', 'South Carolina', '!!!VALENTINA!!!', 'Virginia', 'New York'

# add a single item at the end of the list
usa_states_name.append("NEW STATE HERE")
print(usa_states_name)  # 'Alaska', 'Hawaii', 'NEW STATE HERE']

# extend the list means add a list of multiple items at the end of the list
usa_states_name.extend(["NEW STATE", "NEW STATE 2", "NEW STATE 3"])
print(usa_states_name)  # 'Alaska', 'Hawaii', 'NEW STATE HERE', 'NEW STATE', 'NEW STATE 2', 'NEW STATE 3']

