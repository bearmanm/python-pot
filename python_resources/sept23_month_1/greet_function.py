#for logic, see sublime Python-greeting.py

def greeting(name):
    print('Hello', name)

while True:
    user_name = input('Enter your name:\n')
    greeting(user_name)
    continue_greeting = input('Do you want to continue? (y/n):\n')
    
    if continue_greeting != 'y':
        break

print('Goodbye!')
