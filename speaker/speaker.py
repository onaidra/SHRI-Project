import pyttsx3


class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume', 5.0)

        self.engine.setProperty('rate', 140)

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'italian+f3')

    def speak(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
