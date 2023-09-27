#computer_choice = 'scissors'
#user_choice = input('Do you want to play rock, paper or scissors Matt? (yes/no):\n')
#if user_choice.lower() =="yes":
  #print("Great! which do you want? Rock, Paper or Scissors?\n")
#elif user_choice.lower() == "no":
  #print("Chicken!!! you must be scared you are going to lose!")
#else: 
  #print("Invalid input. Please type yes or no")
  


#computer_choice = 'scissors'
#if computer_choice == user_choice: 
  #print('No one Wins, we have tied')

#elif user_choice == 'rock' and computer_choice == 'scissors':
 #print("XXXX You are the WINNER! XXXX")
#elif user_choice == 'paper' and computer_choice == 'rock':
 #print("XXXX You are the WINNER! XXXX")
#elif user_choice == 'scissors' and computer_choice == 'paper':
 #print('XXXX You are the WINNER! XXXX')
#else:
    #print('you are the losser, the computer wins this time!! :)')

# In summary, this code still simulates a Rock-Paper-Scissors game between the user and the computer. 
# The user is now prompted twice for their choice, and the outcome of the game is determined based on the choices made by both parties.
# still working on how to use the yes/no input 


while True:
 user_choice = input('Do you want to play rock, paper or scissors Matt? (yes/no):\n')

 if user_choice.lower() == "yes":
    user_choice = input("Great! Which do you want? Rock, Paper, or Scissors?\n")
    if user_choice.lower() in ["rock", "paper", "scissors"]:
        print("You chose {user_choice.capitalize()}!")
        break
    else: 
     print("Invalid choice. Please choose Rock, Paper, or Scissors.")
 elif user_choice.lower() == "no":
    print("Chicken!!! You must be scared you are going to lose!")
    break
 else:
    print("Invalid input. Please type yes or no")