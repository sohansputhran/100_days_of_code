height = float(input("Enter your height in m: ")) 
weight = float(input("Enter your weight in kg: "))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
print("Good BMI is between 18.5 and 24.9 for adults.")
print("Your BMI is:", round(bmi,2))
