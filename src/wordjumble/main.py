from utils import * # importing functionss from the helpers file
import os

def main(file):
    
    clearTerminal()

    tprint("WORD JUMBLE")
    # introduction / welcoming the player.
    print("                                           \033[35m" + "WELCOME" + "\033[0m")
    print("In this game, you are given a JUMBLED word - you have to \033[34mUNJUMBLE\033[0m it to move to the next round, and eventually levels.\n"
          "To UNJUMBLE a word is to reorder the given characters to match the sequence of characters of the hidden word.\n"
          "Example, for the word DOG, jumbled -> \033[36m[D G O]\033[0m. You would have to reorder these characters correctly into \033[36mD O G\033[0m to win the round.\n")
    
    print("\nPress SPACE or ENTER to start, press 'Q' to quit the game.")

    try:
        k = readkey()
        if (k == key.SPACE or k == key.ENTER):
            clearTerminal()
        elif (k == 'q'):
            clearTerminal()
            sys.exit(0)

        level_words = getWords(file)
        # testing game by interating through the words... this is not the final logic of the program.
        for word in level_words:

            word = word.lower()
            play(word)

    except(KeyboardInterrupt):
        clearTerminal()
        sys.exit("Game interrupted by user. Exiting")

if __name__ == "__main__":

    file = "../../assets/words/easy_words.txt"
    main(file)
