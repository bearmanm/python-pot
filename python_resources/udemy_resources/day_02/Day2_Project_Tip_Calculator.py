# build a tip calculator using everything you have learnt, your program must include: 
# a greeting, total bill, percentage of tip, quantity of people with an output of how much people should pay with 
# two decimal places. 

greeting = ("Welcome to my tip calculator.")
print(greeting)
total_bill = float(input("What was the total bill? £ "))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
guests = int(input("How many people to split the bill? "))

split = total_bill / guests
tip = split * perc
divide = tip / 100
total = split + divide
pay = round(total, 2)
pay = "{:.2f}".format(total)
print(f"Each person should pay a total of: £ {pay} ")

# note: pay = "{:.2f}".format(total) 
# turns this float(total) to a str "{:.2f}" which abids by this two decimal places format rule "{:.2f}".format