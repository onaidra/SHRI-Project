from speaker.speaker import Speaker
from listener.listener import Listener
from agent.agent import Agent

speaker = Speaker()
listener = Listener()
agent = Agent(speaker, listener, '')

speaker.speak('Ciao sono sara, come posso aiutarti?')

a=False
while a==False:
    command,taken=listener.listen()
    #command, taken = input(), True # ASR cut-off (use console instead)
    command = command.capitalize()

    if command=='Arrivederci':
        speaker.speak("Graziee, a presto")
        break

    if taken==False:
        print("Sara: Non ho capito, puoi ripetere?")
        a=False

