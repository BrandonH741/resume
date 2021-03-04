#Welcome! The purpose of this program is to make a Hangman Game using python. It starts by presenting the user with the
#option to either enter a word to be used, or type 'random' to have the program select a random word from a preset list
#that is saved as a text file. Then it will display the number of blanks, the incorrect letters guessed, and the
#number of guesses left until they are "hanged". A box will be prompting the user to enter a letter/guess. If the guess is
#in the word, the program will fill in the corresponding blank, say the letter was there "x" times, and prompt the user to
#guess again. If it is not, then the program will add the letter to the list of incorrect guess, lower the guess remaining
#counter by one, say it is not there, and prompt the user to guess again. The program ends when either the user guesses all
#the letters in the word or runs out of guesses. At this point, the program will congratulate the victory or bemoan the
#loss, either way asking the user if they want to play again. If they say "yes", then the program will restart; if they say
#no, then the program will wish them farewell.

import random

again = 'yes'

def printing():
    print(blanks)
    print('Guesses left: ', guesses_left)
    print('Guessed letters: ', guessed_letters)
    
print('Welcome to Hangman!')

while again == 'yes':
    word = input('To start, enter a word to be used, or "random" to have the computer pick one for you: ')
    word = word.lower()

    if word == 'random':
        with open('hard_hangman_words.txt', 'r', encoding = 'UTF8') as words:
            word = random.choice(words.read().split())
    elif word == 'easy': #for future additions
        with open('easy_hangman_words.txt', 'r', encoding = 'UTF8') as words:
            word = random.choice(words.read().split())

    blanks = '_ ' * len(word)
    guesses_left = 6
    guessed_letters = ''
    printing()
    
    while guesses_left > 0 and '_' in blanks:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        guess = guess[0]
    
        if guess in word:
            index_loop = 0
            for x in word:
                if x == guess:
                    blanks = blanks.split()
                    blanks[word.index(x, index_loop)] = x
                    new = ''
                    for y in blanks:
                        new += y + ' '
                    blanks = new
                    index_loop = word.index(x, index_loop)+1
        elif guess in guessed_letters:
            pass
        else:
            guesses_left -= 1
            guessed_letters += guess + ' '
        printing()
    if '_' not in blanks:
        print('Congratulations! You win!')
    else:
        print('Too bad! Better luck next time!')
        print('The word was: ', word)
    again = input('Would you like to play again? "Yes" or "No"? ')
    again = again.lower()
    if again == 'yes':
        print('Awesome!')
    else:
        print('See you next time!')
    