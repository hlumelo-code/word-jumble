import json
from pathlib import Path
import time 
from os import sys

state_file = Path(__file__).parents[2].resolve() / "assets/state/state.json"
words_file = Path(__file__).parents[2].resolve() / "assets/words/words.json"

def saveState(words):
    """
        SAVESTATE saves the current state of the game. 

        input: list of currently unused words from the state.json file.
        output: saves these words in the state.json file for continuing from it the next time player opens game.

    """
    with open(state_file, "r") as pre:

        content = json.load(pre)
        content['words'] = words
        

    with open(state_file, "w") as post:

        json.dump(content, post)


def restoreState():
    """
        RESTORESTATE - restores all the original words of the game back to the state.json file. this is for cases where the json file
        has been deleted accidentally (or intentionally), if if the player has finished all words and wants to start game from scratch.

    """
    try:

        with open(words_file, "r") as original:
            
            content = json.load(original)

        with open(state_file, "w") as copy:

            json.dump(content, copy)

    except(FileNotFoundError):
        print("Something went wrong when rewriting state file!")
        time.sleep(1)
        sys.exit(1)


def checkState(words):
    """
        inputs: list from the state.json file.
        returns: True if the total len is > 0, meaning there are items in list. 
                    False if the total len is 0, meaning there are no items in list.
    """
    if (len(words) > 0):
        return True # there are still items in lists
    return False



def getState():
    """
        this function is for checking the current state of the game when the player starts the game. this function will determine if the player
        still has unplayed words to go through, and will then lead to them being provided... if not, then it will help to know when to reload all words 
        when list is empty.
    """
    try:

        data = json.loads(state_file.read_text()) #json file data read as text and loaded as json to lists.

        if checkState(data['words']) == True:
            return data['words']

        else:
            restoreState()
            data = json.loads(state_file.read_text())
            return data['words'] 

    except(FileNotFoundError): # if file has been deleted by user/ has been removed.

        restoreState()
        data = json.loads(state_file.read_text())
        return data['words'] 

    except(json.JSONDecodeError):
        print(f"Something went wrong with JSON format: {e}")
        time.sleep(1)
        sys.exit(1)

    
