import speech_recognition as sr
import getpass
from colorama import init
from termcolor import colored

botName=colored('Sara','yellow')
userName=colored(getpass.getuser(),'green')
class Listener():

    def __init__(self):
        return

    def listen(self):
        r=sr.Recognizer()
        mic= sr.Microphone()
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print(botName+": Ti ascolto. . .")
            audio=r.listen(source,phrase_time_limit=10)
            #phrase_time_limit=5
            sentence=""
            taken=True
            try:
                sentence=r.recognize_google(audio, language='it-IT')
                
                print(userName,": ", sentence)

            except sr.UnknownValueError:                        
                taken=False


        return sentence,taken


