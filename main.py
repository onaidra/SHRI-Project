from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent
from colorama import init
from termcolor import colored

speaker = Speaker()
listener = Listener()
agent = Agent(speaker, listener)
botName=colored('Sara','yellow')

speaker.speak('Ciao sono Sara, come posso aiutarla?')
print('Ciao sono '+botName+', come posso aiutarla?')
a=False
while a==False:
    command,taken=listener.listen()
    command = command.capitalize()

    if command=='Arrivederci':
        speaker.speak("Graziee, a presto")
        break

    if taken==False:
        print(botName+": Non ho capito, puoi ripetere?")
        a=False
    agent.think_man(command)
