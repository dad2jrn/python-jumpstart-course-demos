import random

print('-------------------------------------------')
print('            Guess that number')
print('-------------------------------------------')
print()

# generate teh random number
rnumber = random.randint(0, 100)
print('I picked a number between 0 and 100.  Try to guess what number I picked!')
print()

# This defined guess before we need it for syntax purposes.
guess = -1
name = input('What is your name? ')
# compare the user's guess to the random number
while guess != rnumber:
    # get user input for the guessed number
    guess_number = input('Please guess a number between 0 and 100. ')
    # convert the user input to integer
    guess = int(guess_number)
    if guess > rnumber:
        print('Sorry {0}, but your guess of {1} is higher than my number.'.format(name, guess))
    elif guess < rnumber:
        print('Sorry {0}, but your guess {1} is lower than my number.'.format(name, guess))
    else:
        print('GREAT JOB!!! You guessed right.')
print('Game Over!')
