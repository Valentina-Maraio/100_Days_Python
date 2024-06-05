height = input("How tall are you? ")
weight = input("How do you weight? ")

bmi = int(weight) / (float(height) ** 2)

print(int(bmi))

# Round number
print(8 / 3)  # 2.6666666666666665
print(int(8 / 3))  # 2
# this gives me the same result as the previous one:
print(8 // 3)  # 2
print(round(8 / 3))  # 3
print(round(8 / 3, 2))  # 2.67

# I can keep calculate over a result I get
result = 4 / 2
result /= 2
print(result)  # 1.0

# f string
score = 0
height = 1.8
isWinning = True

print(f"These are the data: The score: {score}, he's height: {height}, He won: {isWinning}")

