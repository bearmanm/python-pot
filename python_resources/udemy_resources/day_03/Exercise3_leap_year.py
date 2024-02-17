# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 

# This is how you work out whether if a particular year is a leap year.

# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder
    
year = int(input("enter the year\n")) # 1900 or 2000
if year %4 ==0 and (year %100 !=0 or year %400 ==0): #two variables need to be the same for this to become a True or a False statement
    print("Leap year")
else:
    print("Not leap year")
    
if year %2000 ==0:
     
# 1900/4=475 no reminder, so True
# 1900/100=19 no remainder, so False (condition asks != NOT equal to)
# 1900/400=4.75 with remainder, so False (condition asks ==0 no remainder)
#True, False or False = else: print(Not leap year)

# 2000/4=500 no reminder, so True
# 2000/100=20 no remainder, so False (condition asks != NOT equal to)
# 2000/400=5 with remainder, so True (condition asks ==0 no remainder)
#True, False or True = if: print(leap year)
