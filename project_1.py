#program 1 [Snake,Gun & Water] Game
import random
def game(user,comp):
    if user==comp:
        print("It's a tie..")

    elif (user=='Snake'and comp=='Water') or (user=='Water'and comp=='Gun') or (user=='Gun'and comp=='Snake') :
        print('Congrats!You WON this game..')    

    else:
        print("Oop's! You lose this time....")

print('''hey  guys,Welcome to  my 1st python project hope you like it...''')
print('''    Snake,Water & Gun game  ''')
i=1
while i<=3:
  options=['Gun','Water','Snake']
  comp=random.choice(options)
  user=input('Enter your choice:')
  user=user.capitalize()
  print(f'My choice :{comp}')

  game(user,comp)
  print(f'You have {3-i} chances left')
  i+=1
print('Gamme Over')

