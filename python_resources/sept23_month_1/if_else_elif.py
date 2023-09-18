# An if statement
# an if statement lets us decides us what to do: if True, then do this. 

temperature = 95 #assign a value to the temperature variable (95)
if temperature > 80: #is the temperature greater than 80? which the value leads to True. so these two line below are run
    print("It's too hot!")  
    print("Stay inside")  
# any indented code that comes after an if statement is called a CODE BLOCK. so the two print() lines above, are known as CODE BLOCK.
   
temperature = 75  
if temperature > 80: # this is False, so the print lines are NOT run, because 75 is not greater than 80. 
    print("It's too hot!")  
    print("Stay inside") 

  
# so how do we do something else here if this is False? 
# we can use an else statement
else:
    print("Enjoy the outdoors!")
# so an if statement is True, we run the CODE BLOCK that is indented below it, 
# otherwise we'll run the indented CODE BLOCK beneath the else statement. 
# so in this case our temperature is NOT greater than 80, 'False' so the else CODE BLOCK is run.  	
# what if we want to check another condition, like... what if the temperature is less than 60, print it's too cold, stay inside. 
# we can add another condition by adding an elif check. here we'll check if the temperature is less than 60, 
#then we'll print 'it's too cold stay inside'

#elif temperature < 60:
print("It's too cold!")
print("Stay inside!")


#correct 
temperature = 81 #this value is the variable 
if temperature > 80: 
   print("It's too hot!")
   print("Stay inside")
elif temperature < 60:
    print("It's too cold!")
    print("Stay inside")   
else: 
   print("Enjoy the outdoors")

# only one comparsion needs to be True for the if statement to be True.
# so let's shorten the program to only say: "Stay inside!" OR "Enjoy the outdoors!"
# you can see we are repeating 'print("Stay inside!")' line of code twice. 
# there is a way to combine the first 2 if statements. 
# the keyword 'or' lets you combine multiple comparsions. 

temperature = 81 
if temperature > 80 or temperature < 60:
   print("Stay inside") 
else: 
   print("Enjoy the outdoors")