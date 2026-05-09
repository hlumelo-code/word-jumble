from utils import * # importing functionss from the helpers file
import os
from sounds import *

def main(file):
    """
        this is the main funtion of the game. it is the first function the player will interact with when they play the game.

        input: a string name of the file from the assets directory that contains the words that will be used in the game.
        outputs: currently does not return anything but calls the play() function from the utils module that is interactive
                    with the user. 

                    1. i plan to make it return outputs/progress for saving the state of the game soon.
                    2. i want to save the state in a easy-accessable file, like a JSON file.
                    3. i want the game to select words randomly from each level of difficulty.
                    4. i want the game to also be able to be able to switch levels of difficulty after each level is complete.
    """
   
    try:
        clearTerminal()

        tprint("WORD JUMBLE")
        openSound()
        time.sleep(0.3)

        # introduction / welcoming the player.
        print("                                           \033[35m" + "WELCOME" + "\033[0m")
        print("In this game, you are given a JUMBLED word - you have to \033[34mUNJUMBLE\033[0m it to move to the next round, and eventually levels.\n"
              "To UNJUMBLE a word is to reorder the given characters to match the sequence of characters of the hidden word.\n"
              "Example, for the word DOG, jumbled -> \033[36m[D G O]\033[0m. You would have to reorder these characters correctly into \033[36mD O G\033[0m to win the round.\n")
        time.sleep(0.3)
        print("\nPress SPACE or ENTER to start, press 'Q' to quit the game.")

        while True:

            k = readkey()
            if (k == key.SPACE or k == key.ENTER): # chooses to play
                # play sound for choosing to play.
                
                level_words = getWords(file)

                for word in level_words:

                    word = word.lower()
                    play(word)

            elif (k == 'q'): # chooses to quit
                clearTerminal()
                sys.exit(0)

            else: # invalid input
                print("INVALID INPUT", end="", flush=True)
                time.sleep(1)
                print("\r" + " " * 30, end="\r", flush=True) 
                continue

    except(KeyboardInterrupt):
        clearTerminal()
        sys.exit("GAME INTERRUPTED BY USER")

    except(FileNotFoundError):
        clearTerminal()
        sys.exit("ASSETS FOR RUNNING PROGRAM NOT FOUND")

if __name__ == "__main__":

    file = "../../assets/words/easy_words.txt"
    main(file)
