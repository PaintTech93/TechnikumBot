import speech_recognition as sr

def myCommand():
    #Initialize the recognizer
    #The primary purpose of a Recognizer instance is, of course, to recognize speech.
    r = sr.Recognizer()
    #engine = pyttsx3.init()

    with sr.Microphone() as source:
        print('Technikum Bot is Ready...')
        r.pause_threshold = 1
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        #listens for the user's input
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')


    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command
