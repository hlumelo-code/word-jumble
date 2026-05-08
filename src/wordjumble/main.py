from utils import * # importing functionss from the helpers file
import os

def main(file):
   
    try:
        clearTerminal()

        tprint("WORD JUMBLE")
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
        sys.exit("Game interrupted by user. Exiting")

if __name__ == "__main__":

    file = "../../assets/words/easy_words.txt"
    main(file)
