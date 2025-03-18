print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

no_people = int(input("How many people to split the bill? "))

each_share = (total_bill * (1 + tip_percentage * 0.01)) / no_people
each_share = round(each_share, 2)

print(f"Each person should pay: {each_share}")
