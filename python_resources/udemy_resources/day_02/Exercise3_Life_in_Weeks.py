#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:

#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.

#hint: There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = input() # 50
# 90years = 4680weeks
years_minus_age = int(90) - int(age)
age_in_weeks = years_minus_age * 52
print(f"You have {age_in_weeks} weeks left.")
# = You have 2080 weeks left. (crikey!) 
