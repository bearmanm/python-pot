

hair_lenght = int(input("what is you hair lenght in inches?\n"))

if hair_lenght >=12: 
    print("Your hair needs a CUT!")
    dye = int(input("How many months ago since you last had it dyed?\n"))
    if dye >=6:
        print("You could do with your hair being dyed soon!")
    elif dye <5: 
        print("ok, we'll have to wait a bit before we dye it again!")
else: 
    print("your hair needs to GROW!")

