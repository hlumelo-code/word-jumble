import nava
from nava import NavaBaseError

def openSound(): # sound for starting the game

    try:
        sound_file = "../../assets/sounds/start.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def keyPressSound(): # sound for when the player presses key for input

    try:
        sound_file = "../../assets/sounds/key_press.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def winSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/win.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def loseSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/lose.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def backspaceSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/backspace.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")

def invalidSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/faaah.wav"
        nava.play(sound_file, async_mode=True)

    except NavaBaseError as e:
        print(f"SOUND ERROR: {e}")


