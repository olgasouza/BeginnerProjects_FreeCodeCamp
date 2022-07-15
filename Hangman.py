# 12 Beginner Python Projects - FreeCodeCamp
# Hangman

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    print("\n==== THE HANGMAN GAME ====")
    word = get_valid_word(words)
    word_letters = set(word) # saves all the letters in a word as a set
    alphabet = set(string.ascii_uppercase) # list of english characters
    used_letters = set() #to keep track of what the user has already guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        print(f'You have {lives} lives left. You have already used these letters: ', ' '.join(used_letters))
        
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('\nCurrent word: ', ' '.join(word_list))


        user_input = input("Guess a letter: ").upper()
        if user_input in alphabet - used_letters: #if the letter is in the alphabet and I haven't used it yet
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)

            else:
                lives = lives - 1
                print('\nLetter not in word')

        elif user_input in used_letters:
            print("\nYou have already guessed that letter!")

        else:
            print('\nInvalid character')

# gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('\nYou died, sorry. The word was', word)
    else:
        print('\nYou guesses the word', word, '!!')

def play_again():
    resp = 'x'
    while resp != 'n':
        print(hangman())
        resp = input("Play again? y/n: ")
    else: 
        print("Goodbye")

print(play_again())
