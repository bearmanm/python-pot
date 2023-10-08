# elif

print("Welcome to the mikey's rollercoaster ride!")
print("Your must be over 120cm in height to ride on my rollcoaster!")

height = int(input("what is your height in cm?\n"))

if height >=120:
    # if the condition is True 
    print("You can ride on mikey's rollercoaster! ")
    age = int(input("What is your age? "))
    if age <12:
    # if the condition is True
        print("Please pay £5.")
    # elif between 12-18 the condition is True
    elif age <=18:
        print("Please pay £7. ")
    # else the condition is False if 19 or over
    else:
        print("Please pay £12. ")
else:
    # if the condition is False for height. 
    print("Sorry, you need to grow more before you can ride.. you need to eat more chocolate!!")

# >= greater than equal to. <= less than equal to. 