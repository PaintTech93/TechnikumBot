import pyttsx3
from pygame import mixer

engine = pyttsx3.init()


# Voice IDs pulled from engine.getProperty('voices')
# These will be system specific
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('voice', en_voice_id)

def talk(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.say(audio)
    engine.runAndWait()
