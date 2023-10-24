#Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
#Based on a user's order, work out their final bill.
#Small pizza (S): $15
#Medium pizza (M): $20
#Large pizza (L): $25
#Add pepperoni for small pizza (Y or N): +$2
#Add pepperoni for medium or large pizza (Y or N): +$3
#Add extra cheese for any size pizza (Y or N): +$1


print("Thank you for choosing Mikey's Pizza Deliveries!")  
pizza_order = input("what size pizza do you want? S, M or L?\n")

add_pepperoni = input("do you want pepperoni? Y or N\n")
extra_cheese = input("do you want extra cheese? Y or N\n")
bill = 0
if pizza_order == str("S"):
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif pizza_order == str("M"):
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif pizza_order ==str("L"):
    bill = 25 
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
  
print(f"Your final bill is: £{bill}.")