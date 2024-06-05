age = input("How old are you? ")

weeks_in_a_year = 52
weeks_in_90_years = int(weeks_in_a_year) * 90

weeks_til_today = int(age) * int(weeks_in_a_year)

weeks_left = weeks_in_90_years - weeks_til_today
weeks_left_in_years = weeks_left / weeks_in_a_year
print(f"You have {weeks_left} weeks left.")
print(f"Which are {weeks_left_in_years} years.")