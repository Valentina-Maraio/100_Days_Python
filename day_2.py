# Welcome to the tip Calculator!
greetings = "Welcome to the tip calculator!"
print(greetings)
bills_cost = float(input("What was the total bill? "))
tip_value = input("How much tip would you like to give? 10, 12, or 15? ")
num_of_people = input("How many people to split the bill? ")
chosen_tip = float(tip_value) / 100
tip_to_bill = bills_cost * float(chosen_tip)
to_pay = int(bills_cost) + int(tip_to_bill)
each_person_has_to_pay = round(to_pay / int(num_of_people), 2)
# if I have a bill that looks like this: 44.60 I should write this:
final_amount = "{:.2f}".format(each_person_has_to_pay)
print(f"Each person should pay: ${final_amount}")
