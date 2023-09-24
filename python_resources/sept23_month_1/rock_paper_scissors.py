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
