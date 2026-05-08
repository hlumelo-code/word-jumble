import nava

def openSound():

    try:
        sound_file = "../../assets/sounds/start.wav"
        nava.play(sound_file, async_mode=True)

    except(FileNotFoundError):
        print("SOUND FILE NOT FOUND")

