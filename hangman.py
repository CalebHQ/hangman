import random
import os
import sys

images = [
    '''
    -+----+
          |
          |
          |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
          |
          |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
          |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
     |    |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
    /|    |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
    /|\   |
          |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
    /|\   |
    /     |
        __|_
    ''',
    '''
    -+----+
     |    |
     O    |
    /|\   |
    / \   |
        __|_
    '''
]

words = ['hello', 'goodbye', 'greetings', 'welcome', 'hungry', 'dictionary', 'people', 'alien', 'beginning', 'ending', 'story', 'book', 'heart', 'love',
         'friendship', 'family', 'brother', 'mother', 'father', 'sister', 'moonlight', 'university', 'school', 'primary', 'secondary', 'secret', 'talking', 'experience']

MAX_GUESSES = 8
guesses = 0

word = random.choice(words).upper()

word_template = []


def title(word):
    print('''
    █░█ ▄▀█ █▄░█ █▀▀ █▀▄▀█ ▄▀█ █▄░█
    █▀█ █▀█ █░▀█ █▄█ █░▀░█ █▀█ █░▀█''')

    for letter in word:
        word_template.append('_')

    for x in word_template:
        print(x, end=' ')
    print('')


def guess_input():
    while True:
        guess = input('Guess: ').upper()
        if len(guess) == 1:
            break

        print('Invalid, try again')

    return guess


def restart():
    print('')
    again = input('Again? (y/n): ')
    if again == 'y':
        word = random.choice(words).upper()
        os.system('cls')
        word_template.clear()
        title(word)
        game(word)
    else:
        sys.exit()


def game(word):
    wrong_letters = []
    right_letters = []

    guesses = 0
    while guesses < MAX_GUESSES:
        guess = guess_input()
        os.system('cls')

        if guess in word:
            if guess not in right_letters:
                right_letters.append(guess)
                print('Right!')
                print('')
                for n in range(len(word)):
                    if word.find(guess, n) == n:
                        word_template[n] = guess
            else:
                print('Already Guessed that')
                print('')
        else:
            if guess not in wrong_letters:
                wrong_letters.append(guess)
                print('Wrong!')
                print(images[guesses])
                guesses += 1
            else:
                print('Already Guessed that')
                print('')

        for x in word_template:
            print(x, end=' ')
        print('')

        if len(wrong_letters) >= 1:
            print('Wrong Letters: ', end='')
            for x in wrong_letters:
                print(x, end=' ')
            print('')

        print(f'Guesses Left: {MAX_GUESSES - guesses}')
        print('')

        if '_' not in word_template:
            print('You win!')
            restart()

    print('You lost!')
    restart()


if __name__ == '__main__':
    title(word)
    game(word)
