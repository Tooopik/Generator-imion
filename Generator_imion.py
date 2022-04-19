from random import randint

name = ['John', 'Thomas', 'Micke', 'Chris', 'Louis', 'Alice', 'Elen', 'Judy']
surname = ['Smith', 'Jones', 'Williams', 'Taylor', 'Davies', 'Brown', 'Evans']
userChoice = 'y'
print('Welcome in name generator!')

while userChoice == 'y':
    print('Do you want generate your new name (y/N)')
    userChoice = input('>>> ')
    if userChoice == 'y':
        print(
            f'Your new name is {name[randint(0,len(name))-1]} {surname[randint(0,len(surname))-1]}')
