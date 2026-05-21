from utils import * # importing functionss from the helpers file
import os
from sounds import openSound
from state import getState

def main():
    """
        this is the main funtion of the game. it is the first function the player will interact with when they play the game.

        input: a tuple of lists that contain the words that will be used in the game.
        outputs: returns a tuple of lists of the unused words in the game that will be saved in state file. 
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
                # do something when player chooses to play...
                print(getState())
                sys.exit(0)

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


if __name__ == "__main__":

    main()

    
