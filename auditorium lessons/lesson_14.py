# Banker Roulette
import random

persons = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

names_items = len(persons)
random_choice = random.randint(0, names_items-1)
choice = int(random_choice)

who_s_going_to_pay = persons[choice]

print(f"{who_s_going_to_pay} is going to buy the meal today!")

# Nested list
fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears', 'Tomatoes']
vegetables = ['Spinach', 'Kale', 'Celery', 'Potatoes']
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

good_omens = [
    ['Aziraphale', 'Tea cups', 'Travel sweets', 'Ring', 'Halo'],
    ['Crowley', 'Wine', 'Snake', 'Yellow eyes', 'Bentley']
]
in_love = 'Aziraphale loves Crowley'
in_love_and_kiss = 'Crowley loves Aziraphale'
good_omens[0].append(in_love)
good_omens[-1].append(in_love_and_kiss)
print(good_omens)

fruits_test = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']
vegetables_test = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']
new_dozen = [fruits_test, vegetables_test]
print(new_dozen[1][1])