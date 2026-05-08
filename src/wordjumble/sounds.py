import nava

def openSound(): # sound for starting the game

    try:
        sound_file = "../../assets/sounds/start.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

def keyPressSound(): # sound for when the player presses key for input

    try:
        sound_file = "../../assets/sounds/key_press.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

def winSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/win.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

def loseSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/lose.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

def backspaceSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/backspace.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

def invalidSound(): # sound for when the player wins a round

    try:
        sound_file = "../../assets/sounds/faaah.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")


