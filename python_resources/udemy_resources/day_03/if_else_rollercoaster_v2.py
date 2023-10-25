# my program
print("Welcome to the mikey's rollercoaster ride!")
print("Your must be over 120cm in height to ride on my rollcoaster!")

height = int(input("what is your height in cm?\n"))
if height >=120:
    
    print("You can ride on mikey's rollercoaster! ")

    age = int(input("What is your age? "))
    if age <12:
     photo1 = input("Do you want a photo taken?\n")
     if photo1 ==str("yes"):
      print("that will cost £3 extra")   
      print("Please pay £8.")
     if photo1 ==str("no"):
      print("Please pay £5.")
    
    elif age <=18:
     photo2 = input("Do you want a photo taken?\n")
     if photo2 ==str("yes"):
         print("that will cost £3 extra")
         print("Please pay £10.")
     if photo2 ==str("no"):
      print("Please pay £7. ")
    # else the condition is False if 19 or over
    else:
     photo3 = input("Do you want a photo taken?\n")
     if photo3 ==str("yes"):
         print("that will cost £3 extra")
         print("Please pay £15.")
     if photo3 ==str("no"):
      print("Please pay £12. ")
else:
    # if the condition is False for height. 
    print("Sorry, you need to grow more before you can ride.. you need to eat more chocolate!!")

# Udemy program   
print("Welcome to the rollercoaster ride!")
print("Your must be over 120cm in height to ride on this rollcoaster!")

height = int(input("what is your height in cm?\n"))
bill = 0

if height >=120: 
    print("You can ride on this rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are £5.")
    elif age < 18:
        bill = 7
        print("junior tickets are £7.")
    elif age >= 45 and age <= 55:
        print("Adults between 45 - 55 ride for free.")
    else:
        bill = 12
        print("Adult tickets are £12.")
    wants_photo = input("Do you want photo? Y or N.\n")
    if wants_photo == "Y":
        bill += 3    

    print(f"Your final bill is £{bill}\n")
else:
    print("Sorry, you need to grow more before you can ride!")