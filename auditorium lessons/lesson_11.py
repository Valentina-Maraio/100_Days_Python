valore_1 = 12
valore_2 = 15

if valore_1 > 10 and valore_1 < 13:
    print("TRUE")
else:
    print("FALSE")

if valore_1 > 10 and valore_2 < 13:
    print("TRUE")
else:
    print("FALSE")

if valore_1 > 10 or valore_1 < 13:  # TRUE
    print("TRUE")
else:
    print("FALSE")

if valore_1 > 10 or valore_2 < 13:  # TRUE
    print("TRUE")
else:
    print("FALSE")

if not valore_1 > 10 and valore_1 < 13:  # FALSE
    print("TRUE")
else:
    print("FALSE")

# Python Pizza Delivery
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L. ")  # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N. ")  # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N. ")  # Do you want extra cheese? Y or N

bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25
print(f"first round: ${bill}.")
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3
print(f"second round: ${bill}.")
if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")

# Logical Operators
# A and B
# both need to be true in order to the all statement to be true.
# C or D
# not E
