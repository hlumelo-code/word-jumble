from utils import *
from sounds import openSound
from state import getState


def main():
    """
        main function - greets the player and asks them to respond/choose if they want to play or quit the game.
            if player presses ENTER or SPACE, the wordjumble() function is called with the list of words unused
            by the player.
            if they press Q, the game shuts down.
            if they use CTRL_X or CTRL_C, the program terminates. 
        
    """
   
    try:
        clearTerminal()

        tprint("WORD JUMBLE")
        openSound()
        time.sleep(0.3)

        # welcoming the player.
        print("                                           \033[35m" + "WELCOME" + "\033[0m")
        print("In this game, you are given a JUMBLED word - you have to \033[34mUNJUMBLE\033[0m it to move to the next round, and eventually levels.\n"
              "To UNJUMBLE a word is to reorder the given characters to match the sequence of characters of the hidden word.\n"
              "Example, for the word DOG, jumbled -> \033[36m[D G O]\033[0m. You would have to reorder these characters correctly into \033[36mD O G\033[0m to win the round.\n")
        time.sleep(0.3)
        print("\nPress SPACE or ENTER to start, press 'Q' to quit the game.")

        while True: # this while loop is for making sure to query the user until a valid input is used.

            k = readkey()
            if (k == key.SPACE or k == key.ENTER): # chooses to play
                words = getState()
                wordjumble(words)
                break

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

    
