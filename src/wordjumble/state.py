import json
from pathlib import Path
import time 
import os

state_file = Path(__file__).parents[2].resolve() / "assets/state/state.json"
words_file = Path(__file__).parents[2].resolve() / "assets/words/words.json"

def saveState(lists):
    """
        this function with save the currently unused words in the game to the json file so the player can pick up where they left off.

        input: tuple containing 3 lists
        output: none, saves lists into state_file.
    """
    with open(state_file, "r") as pre:

        content = json.load(pre)
        content['easy'] = lists[0]
        content['medium'] = lists[1]
        content['hard'] = lists[2]

    with open(state_file, "w") as post:

        json.dump(content, post)


def restoreState():

    """
    This function restores all the words from the words.json file into state.json file for player to use.

        input: None
        outputs: it rewrites the state file from scratch to be in its original form.
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


def checkState(easy, medium, hard):
    """
        inputs: 3 lists from the state.json file.
        returns: True if the total len of all 3 is > 0, meaning there are items in lists. 
                    False if the total len is 0, meaning there are no items in lists.
    """
    if (len(easy) + len(medium) + len(hard) > 0):
        return True # there are still items in lists
    return False

def getState():
    """
        this function is for checking the current state of the game when the player starts the game. this function will determine if the player
        still has unplayed words to go through, and will then lead to them being provided... if not, then it will help to know when to reload all words 
        when all lists are empty.
    """
    try:

        lists = json.loads(state_file.read_text()) #json file data read as text and loaded as json to lists.

        if checkState(lists['easy'], lists['medium'], lists['hard']) == True:
            return lists['easy'], lists['medium'], lists['hard'] # returns a tuple of 3 lists.

        else:
            restoreState()
            lists = json.loads(state_file.read_text()) 
            return lists['easy'], lists['medium'], lists['hard'] # returns a tuple of 3 lists.


    except(FileNotFoundError): # if file has been deleted by user/ has been removed.

        restoreState()
        lists = json.loads(state_file.read_text()) 
        return lists['easy'], lists['medium'], lists['hard'] # returns a tuple of 3 lists.
 
    except(json.JSONDecodeError):
        print(f"Something went wrong with JSON format: {e}")
        time.sleep(1)
        sys.exit(1)

    
