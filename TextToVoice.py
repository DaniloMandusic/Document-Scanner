import pyttsx3

def textToVoice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()