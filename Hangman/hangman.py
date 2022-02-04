"""
Tutorial by Kylie Ying on youtube: https://www.youtube.com/ycubed
Her Github: https://github.com/kying18
"""

import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        print(f'You have {lives} lives left and you have guessed these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print(f'\nThe letter is not in the word.')

        elif user_letter in used_letters:
            print('You have already guessed that letter... Please try again.')
        else:
            print('No such letter in the word. Try again.')

    if lives == 0:
        print('Sorry, you died. The word was', word, '!!')

    else:
        print('Congrats, you win! You have guessed the word:', word, '!!')


print(hangman())
