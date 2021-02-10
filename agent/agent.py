"""agent.py
"""
from agent.interactions import Richieste,Risposte
import re
import random
from colorama import init
from termcolor import colored

botName=colored('Sara','yellow')

database =  {"Rosa":4, "Calla":1.5, "Tulipano":3, "Giglio":3, "Gerbera":1.20, "Margherita":1, "Orchidea":7, "Girasole":4, "Viola":2, "Papavero":0.50,"Fiore di Loto":4,
"Ginestra":0.2, "Crisantemo":0.7, "arancio":0.3,  "Firdaliso":2.5, "Calendula":1, "Lavanda":0.3, "Non ti scordar di me":0.2, "Ortensia":2, "Peonia":1.5, "Mimosa":3,"Giacinti":8,
"Narcisi":1,"Ibisco":1.3,"Magnolie":1.2,"Pesco":0.3, "Acacia":0.3, "Azalea":1, "Anemone":1, "Gelsomino":0.2, "Erica":0.3,  "Iris":1.5, "Sterlitzia":2,"lilla":1,
"Zimnia":1.5,"Bocche di Leone":1,"Eucalipto":0.6,"Amaryllis":1.6,"Fresie":1,"Camelia":0.80}
#print(database["Eucalipto"])
database2 = {"Valentino": ["mazzo San Valentino","Il mazzo ha 13 rose rosse",50], "Matrimonio" : ["bouquet per il matrimonio","Il bouquet ha rose bianche, tulipani e fiori d'arancio",40], 
"Comunione" : ["mazzo per comunione","Il bouquet ha tulipani bianchi, calle, rose bianche e alcuni gigli",60], "Funerale" : ["La corona per un funerale","La corona è composta da rose e calle, rigorosamente bianche",200], 
"Compleanno": ["mazzo per un compleanno","Il mazzo è formato da gerbere e rose gialle o altrimenti un'orchidea",30], "Festa della donna":["mazzo per la festa della donna","Un bellissimo mazzo di mimosa",25],
"Anniversario":["mazzo per l'anniversario","Il mazzo ha 7 rose rosse",35],"Battesimo":["mazzo per il battesimo","Il bouquet ha tulipani bianchi, calle, rose bianche e alcuni gigli",60],
"Fidanzamento":["mazzo per un fidanzamento","Il mazzo ha rose e tulipani rigorosamente rossi",40],"Amica":["mazzo per un amica","Il mazzo prevede un girasole con alcuni tulipani gialli",35]   }

class Agent:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener
        self.prezzo=0

    def think_man(self, command:str):
        varx=command.upper()
        match=find_match(self,varx)

        
        if match == '4':     #tipologia evento
            varx2=command.split()
            db_find(self,varx2)
        
        if match=='5':
        
            if self.prezzo==0:
                print(botName+": Non ho capito di cosa vuole sapere il prezzo")
                self.speaker.speak("Non ho capito di cosa vuole sapere il prezzo")
            else :
                pr="Il costo è di "+str(self.prezzo)+" euro"
                print(botName+": "+pr)
                self.speaker.speak(pr)

        if match==False:
            print(colored(botName+": Mi dispiace non abbiamo nulla",'red'))
            self.speaker.speak("Mi dispiace non abbiamo nulla")


def find_match(self,command):
    print("find_match")
    for k in Richieste:
        for i, interaction in enumerate(Richieste[k]):
            match = re.search(interaction.upper(),command)
            if match:
                print(botName+": "+Risposte[k][0])
                self.speaker.speak(Risposte[k])
                return k
    return False



def db_find(self,varx2):
    print("db_find")
    for v in varx2:
        v=v.capitalize()
        if v in database2.keys():
            nome=v
            nomeMazzo=database2[nome][0]
            descrizioneMazzo=database2[nome][1]
            self.prezzo=database2[nome][2]
            text1="Che ne pensa di questo "+nomeMazzo+"?\n"+descrizioneMazzo
            print(botName+": "+text1)
            self.speaker.speak(text1)
'''   
    def think_man(self, command):
        try:
            command=command.split(" ")
            for i in command:
                i=i.capitalize()
                if i in database:
                   value=(database[i])
                   print(value)
        except:
            print("Non ho capito scusa")  
'''

