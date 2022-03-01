#!/usr/bin/env python3

import requests
import random


def get_word(url):
    """Return a random word from a .json file on the specified url. (the .json has only one key named 'data',
    and it's value is a list of words """
    response = requests.get(url)
    json_data = response.json()
    words = json_data['data']
    word = random.choice(words)
    return word


def hangman(word):
    """Give it a word and let the game begin"""
    print('Welcome to Hangman\nYou dare to play?')
    # Choosing a hint letter to show from the beginning
    # and creating the partially hidden word to show up.
    random_letter = random.choice(word)
    displayed_word = []
    for letter in word:
        if letter == random_letter or letter == '-':
            displayed_word.append(letter)
        else:
            displayed_word.append('_')
    # Showing the hidden word and initializing counter of failed tries,
    # the initial hangman image, and the tried letters.
    print(''.join(displayed_word))
    counter = 0
    hang = '---\n'
    tried_letters = []
    # Looping until the word is guessed or the count reaches 4:
    while ''.join(displayed_word) != word and counter < 4:
        guess = input('Try a letter.\n')
        if guess not in tried_letters:
            tried_letters.append(guess)
        # If guessed correctly, the letter is added to the partially hidden word
        if guess in word:
            position = word.index(guess)
            displayed_word[position] = guess
            print(hang + '\n')
            print(''.join(displayed_word))
            print(f'you have tried: {tried_letters}')
        # If wrong guess, the counter and hangman image progress:
        else:
            counter += 1
            if counter == 1:
                hang += ' |'
            elif counter == 2:
                hang += '\n O'
            elif counter == 3:
                hang += '\n-|-'
            else:
                hang += '\n /\\'
            print(hang + '\n')
            print(''.join(displayed_word))
            print(f'you have tried: {tried_letters}')
    # Here the game ends, and we print the win/lose message:
    if counter < 4:
        print('WELL DONE!, YOU WON!')
    else:
        print(f'YOUR NECK IS BROKEN, YOU ARE DEAD.\nThe word was: {word}')


if __name__ == '__main__':
    wrd = get_word('https://www.randomlists.com/data/words.json')
    hangman(wrd)
