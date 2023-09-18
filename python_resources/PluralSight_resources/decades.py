age = int(input("let's work out how many decades old you are?\n")) # step 1
decades = age // 10 # step 3
years = age % 10 # step 4
#user types there age - step 2 
print("You are " + str(decades) + " decades and " + str(years) + " years old") # step 5
# step 6 end

# then to print to a whole number and print out the remaining years 
# python has an special operator for whole number divison or integer divison which is two // so decades would not look like this.. 
#decades = age/10 but in fact would look like age // 10
