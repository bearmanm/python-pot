computer_choice = 'scissors'
user_choice = input('Do you want to play rock, paper or scissors Matt?\n')
user_choice = input('Great! do you want rock, paper,or scissors??\n')

if computer_choice == user_choice: 
  print('No one Wins, we have tied')

elif user_choice == 'rock' and computer_choice == 'scissors':
 print("XXXX You are the WINNER! XXXX")
elif user_choice == 'paper' and computer_choice == 'rock':
 print("XXXX You are the WINNER! XXXX")
elif user_choice == 'scissors' and computer_choice == 'paper':
 print('XXXX You are the WINNER! XXXX')
else:
    print('you are the losser, the computer wins this time!! :)')

# In summary, this code still simulates a Rock-Paper-Scissors game between the user and the computer. 
# The user is now prompted twice for their choice, and the outcome of the game is determined based on the choices made by both parties.
# still working on how to use the yes/no input 
