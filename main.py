from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent
from colorama import init
from termcolor import colored

speaker = Speaker()
listener = Listener()
agent = Agent(speaker, listener)
botName=colored('Sara','yellow')
endCheck = False
speaker.speak('Ciao sono Sara, come posso aiutarla?')
print('Ciao sono '+botName+', come posso aiutarla?')
a=False
while a==False:
    command,taken=listener.listen()
    command = command.capitalize()

    if (command=='Arrivederci' or command=='Ciao' or command=='Alla prossima' or command=='Arrivederla') and endCheck==True:
        speaker.speak("Grazie, a presto")
        break

    if taken==False:
        frase=botName+": Non ho capito, puoi ripetere?"
        print(frase)
        speaker.speak("Non ho capito, puoi ripetere?")
        a=False
    if taken == True:
        agent.think_man(command)
        endCheck=True
