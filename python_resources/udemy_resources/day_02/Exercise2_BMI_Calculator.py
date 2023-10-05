# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. 
# If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# the output must be printed out a as whole number

height = input("enter you height in meters Amy Bearman please    m: ") # 1.76
weight = input("enter your weight in kg as well please Amy     kg: ")  # 80

total_height = float(height) * float(height)
bmi = float(weight) / float(total_height)
print(int(bmi))
# = 25 (means i'm over weight EEK!)
