import random

print('Hello, What are you known as?')
name = input()

print('Hi,'  + name + ' I am thinking of a number between 1 to 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
    
if guess == secretNumber:
    print('Good job,' + name + '! You guessed the number in ' + str(guessesTaken) + ' gusses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))    