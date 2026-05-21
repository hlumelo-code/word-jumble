import nava
from nava import NavaBaseError
from pathlib import Path

"""
    all functions in this module are identical in their purpose, as they fetch sound files from 
    the /assets/sounds directory. they only differ in the sound each function plays.

    input: none
    output: plays sound using the nava sound library. 

                1. async_mode=True allows sound to be played while the program continues to run 
                    without pausing until sound is done playing.
                2. NavaBaseError is the nava exception for catching errors with playing audio files.
"""
root_dir = Path(__file__).resolve().parents[2]

def openSound(): # sound for starting the game

    try:
        sound_file = str(root_dir) + "/assets/sounds/start.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def keyPressSound(): # sound for when the player presses key for input

    try:
        sound_file = str(root_dir) + "/assets/sounds/key_press.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def winSound(): # sound for when the player wins a round

    try:
        sound_file = str(root_dir) + "/assets/sounds/win.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def loseSound(): # sound for when the player wins a round

    try:
        sound_file = str(root_dir) + "/assets/sounds/lose.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def backspaceSound(): # sound for when the player wins a round

    try:
        sound_file = str(root_dir) + "/sounds/backspace.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def invalidSound(): # sound for when the player wins a round

    try:
        sound_file = str(root_dir) + "/sounds/faaah.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")


