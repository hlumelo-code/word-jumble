import os
import csv
import sys
import time
import random
from art import *
from readchar import readkey, key
from sounds import *
from state import saveState

def wordjumble(words): # this is the engine of the game.

    for word in words:

        solved = False
        solved = play(word)

        if solved == True: # if the current word has been solved...
            words.remove(word)
            continue
        else:
            saveState(words)
            break

def clearTerminal():
    """
        this function clears the terminal window. it checks the OS and removes all outputted text from terminal.

        input: none
        output: removes text from terminal window.
    """

    if (os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def play(word): 
    """
        inputs: 
            1. word - the original string the player has to correctly guess.
            2. jumbled - a string containing randomly organized characters from the original string
                that the player will use to reorganize to match the original string.
        outputs:
            this function is the skeleton for the player to solve the character puzzle and also how the user
            interacts with the game using the keyboard. it tracks valid inputs, and handles invalid ones, it 
            also tracks whether the player has already won the game and terminates the round if they won, and 
            replays the round if they lost. it is the fundamental engine of solving the puzzle.. 
    """
    
    try:
            
        player_sorted = [] # list of characters sorte by player input.
        index_stack = [] # a form of a "stack" for tracking the index of each character in case the player backspaces.

        while True: # while the user has not solved the puzzle of the characters...

            jumbled = jumble(word)
            jumbled_list = list(jumbled)
            message = ""
            

            while len(player_sorted) < len(word): # while they have not typed all of the valid characters.
                
                clearTerminal() 
                showProgress(player_sorted, jumbled_list, message) # show progress to the player.
                print("CTRL_C OR CTRL_X TO QUIT\n\n")
                
                player_input = readkey() # taking user input from keyboard.
                
                if (player_input != key.BACKSPACE and player_input in jumbled_list):
                    keyPressSound()
                
                
                if (player_input.isalpha() and player_input[0] in jumbled_list): # if the user typed valid and available chars from jumbled_list

                    index_stack.append(jumbled_list.index(player_input[0])) # append the index of the character that matches playr input to "stack".
                    player_sorted.append(player_input[0]) # add that character to the player sorted list.
                    jumbled_list.remove(player_input[0]) # remove it from the available set of valid randomized characters.
                    message = ""

                elif (player_input.isalpha() and player_input[0] not in jumbled_list and player_input[0] in word): # letter exhausted
                    message = f"YOU HAVE EXHAUSTED THE LETTER {player_input.upper()}"
                    continue

                elif (player_input.isalpha() and player_input[0] not in word):
                    invalidSound()
                    message = f"THE LETTER {player_input.upper()} IS NOT IN THE ORIGINAL WORD."
                    continue

                elif (player_input == key.BACKSPACE): # if player pressed backspce

                    try: 
                        last_value = player_sorted.pop() # get the index of that recent character from the original jumbled string
                        jumbled_list.insert(index_stack.pop(), last_value) # and insert it back to the right index in jumbled string.
                        backspaceSound()
                        message = ""
                        
                    except(IndexError):
                        continue

                elif (player_input == key.CTRL_X) or (player_input == key.CTRL_C) or (player_input == key.CTRL_Z): # player quits
                    raise KeyboardInterrupt

                else:
                    invalidSound()
                    message = "INVALID INPUT. PLEASE TRY AGAIN." # invalid input.
                    
            if (''.join(player_sorted) == word): # player wins the round.
                clearTerminal()
                showProgress(player_sorted, jumbled_list, message)
                print("CORRECT ORDER! LET'S MOVE TO THE NEXT WORD.")
                winSound()
                time.sleep(2)
                clearTerminal()

                return True     # True means they solved this round.
                
            else:
                clearTerminal() # player loses rond / input did not match original string.
                showProgress(player_sorted, jumbled_list, message)
                print("\033[31mTHIS ORDER IS INCORRECT, TRY AGAIN.\033[31m")
                loseSound()
                time.sleep(2)
                player_sorted = []
                jumbled_list = list(jumbled)
                continue
                
    except(KeyboardInterrupt): # player quits game.
        clearTerminal()
        return False


def showProgress(player_sorted, jumbled_list, message = ""):
    """
        inputs:
                1. player_sorted, a list of the characters the player has sorted manually.
                2. jumbled_list, a list of randomly sorted characters from the original secret
                    word that are available to be picked for sorting.
        output:
                an ASCII display of the progress made so far by the player. it will display
                both the user inputted letters and the unpicked ones while they are still available.
                once they are complete, it will only show the final reorganize characters from the player.
    """
    # creating string variables out of lists.
    used_characters = ''.join(player_sorted) 
    unused_characters = ' '.join(jumbled_list)
    # making them capital letters
    used_characters = used_characters.upper()
    unused_characters = unused_characters.upper()

    if (len(jumbled_list)!=0): # if player has not used all available letters/ if they are not done yet
        print("PROGRESS SO FAR")
        tprint(f"{used_characters}")
        print("\033[35mUNUSED LETTERS, PRESS BACKSPACE TO UNDO\033[0m")
        tprint(unused_characters)

    else: # when they are done
        tprint(used_characters)

    if len(message) > 0:
        print(f"\033[31m{message}\033[0m")
    
def jumble(word): # COMPLETE
    """
        input: a string, which is the word that the player has to "UNJUMBLE" ;)
        returns: a string of randomly organized characters from the original string.
    """
    
    letters = list(word)
    jumbled = []

    while len(jumbled) < len(word):
        
        char = random.choice(letters)
        jumbled.append(char)
        letters.remove(char)

        if "".join(jumbled) == word: # if jumbled as a string is the same as origiinal word, restart jumbling.
            jumbled = []
            letters = list(word)

    return "".join(jumbled)


