import random

print('---------------------------------')
print('   GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Sorry %s, your guess of %i was too LOW.' % (name, guess))
    elif guess > the_number:
        print('Sorry %s, your guess of %i was too HIGH.' % (name, guess))
    else:
        print('Excellent work %s, you won, it was %i!' % (name, guess))

print('done')

