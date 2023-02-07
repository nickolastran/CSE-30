# assignment: programming assignment 1
# author: Nickolas Tran
# date: 1/16/2023
# file: hangman.py is a program that the user plays a game by choosing letters and losing lives in the process until the user achieves all the letters in the word
# input: number of letters in a word, number of lives
# output: user guesses letter, falls in a space or loses a life. All lives lost means game over, all spaces filled means they win

from random import choice, random
import os
import random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary(dictionary_file):
    dictionary = {}
    max_size = 12
    read_dict_file = open(dictionary_file, "r" )
    while True:
        lines = read_dict_file.readline().strip()
        if len(lines) == 0:
            break
        try:
            if len(lines) >= max_size:
                length_lines = max_size
            else:
                length_lines = len(lines)
                dictionary[length_lines].append(lines)
        except:
            dictionary[length_lines] = [lines]
    return dictionary

# print the dictionary (use only for debugging)

def print_dictionary (dictionary):
    max_size = 12
    print(dictionary)

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options():
    word_size = random.randint(3,12)
    lives = 5
    try:
        word_size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]:\n"))
        if (word_size >= 3 or word_size < 12):
            print("The word size is set to ", (word_size), ".", sep="")
        else:
            raise Exception
    except:
        print("A dictionary word of any size will be chosen.\n")
    try:
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:\n"))
        print("You have", lives, "lives.")
    except:
        print("You have 5 lives.")
    return (word_size, lives)

# MAIN

if __name__ == "__main__" :
    dictionary = import_dictionary(dictionary_file)
    game = True
    print("Welcome to the Hangman Game!")

# print a game introduction

# set up game options (the word size and number of lives)

# select a word from a dictionary (according to the game options)
# use choice() function that selects an item from a list randomly, for example:
# mylist = ['apple', 'banana', 'orange', 'strawberry']
# word = choice(mylist)

    while game:
        game_opts = get_game_options()
        words = random.choice(dictionary[game_opts[0]]).upper()
        lives = game_opts[1]
        lives_remain = lives
        if ("-" in words):
            c_letter = ["-"]
        else:
            c_letter = []
        g_letter = []

# START GAME LOOP   (INNER PROGRAM LOOP)
# format and print the game interface:
# Letters chosen: E, S, P                list of chosen letters
# __ P P __ E    lives: 4   XOOOO        hidden word and lives

# ask the user to guess a letter

# update the list of chosen letters

# if the letter is correct update the hidden word,
# else update the number of lives
# and print interactive messages

        while lives_remain > -1:
            print("Letters chosen: ", end="")
            print(", ".join(g_letter) + "")
            for i in range(len(words)):
                if words[i] in g_letter:
                    print(words[i] + " ", end="")
                elif (words[i] == "-"):
                    print("- ", end="")
                else:
                    print("__ ", end="")
            print("    lives: " + str(lives_remain) + "   ", end="")
            for x in range(lives):
                if (lives - x - lives_remain > 0):
                    print("X", end="")
                else:
                    print("O", end="")
            if ("".join((sorted(set(words)))) == "".join(sorted(c_letter))):
                print("\nCongratulations!!! You won! The word is " + words + "!")
                break
            if (lives_remain > 0):
                while True:
                    user_int = input("\nPlease choose a new letter >\n").upper()
                    if (len(user_int) > 1 or user_int.isdigit() or user_int == " "):
                        print("Invalid input!")
                    elif (user_int in g_letter):
                        print("You have already chosen this letter.")
                    elif(user_int in words):
                        g_letter.append(user_int)
                        c_letter.append(user_int)
                        break
                    else:
                        g_letter.append(user_int)
                        lives_remain -= 1
                        break
            else:
                print("\nYou lost! The word is " + words.upper() + "!")
                lives_remain -= 1

# END GAME LOOP (INNER PROGRAM LOOP)

# check if the user guesses the word correctly or lost all lives,
# if yes finish the game

# END MAIN LOOP (OUTER PROGRAM LOOP)

# ask if the user wants to continue playing, 
# if yes start a new game, otherwise terminate the program

        if (input("Would you like to play again [Y/N]?\n").upper() == "Y"):
            pass
        else:
            print("Goodbye!")
            break
