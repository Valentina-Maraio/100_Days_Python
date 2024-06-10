# Python Pizza
print("Thanks for choosing Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L. ")
add_pepperoni = input("Do you want pepperoni? Y, N. ")
extra_cheese = input("Do you want extra cheese? Y, N. ")

s = 15
m = 20
l = 25
pepperoni_small = 2
pepperoni_m_l = 3
cheese = 1

if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${s + pepperoni_small + cheese}")  # 18
        else:
            print(f"Your final bill is: ${s + pepperoni_small}")  # 17
    else:
        print(f"Your final bill is; {s + cheese}")  # 16
else:
    print(f"Your final bill is: {s}")  # 15
if size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${m + pepperoni_m_l + cheese}")  # 24
        else:
            print(f"Your final bill is: ${m + pepperoni_m_l}")   # 23
    else:
        print(f"Your final bill is; {m + cheese}")  # 21
else:
    print(f"Your final bill is: {m}")  # 20
if size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            print(f"Your final bill is: ${l + pepperoni_m_l + cheese}")  # 29
        else:
            print(f"Your final bill is: ${l + pepperoni_m_l}")   # 28
    else:
        print(f"Your final bill is; {l + cheese}")  # 26
else:
    print(f"Your final bill is: {l}")  # 25

