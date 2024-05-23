#C:\Users\chery\OneDrive\Documents\Wordle\Wordle
"""Guess-My-Word is a game where the player has to guess a word.
A game in which players put in 5-letters word guesses and see if they match the word of the day!
Players will have 6 attempts to try guess the word correctly.
Author: Xuan Koo
Company: WordsAreUs
Copyright: 2024

"""
# Your code must use PEP8
# Your code must be compatible with Python 3.1x
# You cannot use any libraries outside the python standard library without the explicit permission of your lecturer.

# This code uses terms and symbols adopted from the following source:
# See https://github.com/3b1b/videos/blob/68ca9cfa8cf5a41c965b2015ec8aa5f2aa288f26/_2022/wordle/simulations.py#L104

import random

MISS = 0  # _-.: letter not found ⬜
MISSPLACED = 1  # O, ?: letter in wrong place 🟨
EXACT = 2  # X, +: right letter, right place 🟩

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

ALL_WORDS = 'C:/Users/chery/OneDrive/Documents/Wordle/word-bank/all_words.txt'
TARGET_WORDS = 'C:/Users/chery/OneDrive/Documents/Wordle/word-bank/target_words.txt'


def help():
    """Provides help for the game"""
    print("Welcome to the Guess-My-Word! The objective of the game is to guess a 5-letter word, you have 6 attempts.")
    print("🟩 - Indicates a correct letter in the wrong position")
    print("🟨 - Indicates a correct letter in the correct position")
    print("⬜ - Indicates a letter not in the target word")


def get_valid_words(file_path=ALL_WORDS):
    with open(file_path) as file:
        valid = file.read().split()
    return valid


def get_target_word(file_path=TARGET_WORDS):
    with open(file_path) as file:
        words = file.read().split()
    return random.choice(words)


def ask_for_guess(valid_words):
    guess_word = input("Take a guess at a 5-letter word!").lower()
    if guess_word in valid_words:
        return guess_word
    else:
        print("Please enter a valid 5-letter word")
        return ask_for_guess()


def score_guess(guess, target_word):
    score = []
    for guess_char, target_char in zip(guess, target_word):
        if guess_char == target_char:
            score.append(EXACT)
        elif guess_char in target_word:
            score.append(MISSPLACED)
        else:
            score.append(MISS)
    return tuple(score)


def is_correct(score):
    return all(s == EXACT for s in score)


def format_score(guess, score):
    formatted_guess = ' '.join(guess.upper())
    formatted_score = ' '.join(['🟩' if s == EXACT else '🟨' if s == MISSPLACED else '⬜' for s in score])
    return f"{formatted_guess}\n{formatted_score}"


def play():
    """Code that controls the interactive game play"""
    print(help())
    # Select a word of the day:
    word_of_the_day = get_target_word()
    # Build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()
    # Start the game loop
    for attempt in range(MAX_ATTEMPTS):
        print(f"\nAttempt {attempt + 1}/{MAX_ATTEMPTS}:")
        guess = ask_for_guess(valid_words)
        score = score_guess(guess, word_of_the_day)
        print("\nResult of your guess:")
        print(format_score(guess, score))
        if is_correct(score):
            print("Congratulations! You've guessed the word correctly.")
            break
    else:
        print(f"\nSorry, you've run out of attempts. The word of the day was: {word_of_the_day}")


def main(test=False):
    """Main function to start the game"""
    if test:
        import doctest
        return doctest.testmod()
    play()


if __name__ == '__main__':
    main()
