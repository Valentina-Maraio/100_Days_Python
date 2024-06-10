# BMI 2.0
height = float(input("What is your height?\n"))
weight = input("What is your weight?\n")

your_bmi = int(weight) / float(height ** 2)

if your_bmi < 18.5:
  print(f"Your BMI is {your_bmi}, you're underweight.")
elif 18.5 < your_bmi < 25:
  print(f"Your BMI is {your_bmi}, you have a normal weight.")
elif 25 <= your_bmi <= 30:
  print(f"Your BMI is {your_bmi}, you are slightly overweight.")
else:
  print(f"Your BMI is {your_bmi}, you are obese.")