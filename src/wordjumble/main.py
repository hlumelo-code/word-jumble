from utils import * # importing functionss from the helpers file
import os

def main(word):
    
    clearTerminal()

    tprint("WORD JUMBLE")
    # introduction / welcoming the player.
    print("                                           \033[35m" + "WELCOME" + "\033[0m")
    print("In this game, you are given a JUMBLED word - you have to \033[34mUNJUMBLE\033[0m it to move to the next round, and eventually levels.\n"
          "To UNJUMBLE a word is to reorder the given characters to match the sequence of characters of the hidden word.\n"
          "Example, for the word DOG, jumbled -> \033[36m[D G O]\033[0m. You would have to reorder these characters correctly into \033[36mD O G\033[0m to win the round.\n")
    
    print("\nPress SPACE or ENTER to start, press 'Q' to quit.")

    try:
        while True:   # the while loop to drive the game. breaks on Q or KeyboardInterrupt
            k = readkey()

            if (k == key.SPACE or k == key.ENTER):
                clearTerminal()

                jumbled = jumble(word)
                outcome = unjumble(word, jumbled)

                if outcome == 1:
                    # if they win the round.
                    print("this is the part where you use another word since the player won. for now, i'll exit the game at this point")
                    break
            
            elif (k == 'q'):
                clearTerminal()
                sys.exit(0)

            else:
                continue

    except(KeyboardInterrupt):
        clearTerminal()
        sys.exit("Game interrupted by user. Exiting")

if __name__ == "__main__":

    main("dimensions")
