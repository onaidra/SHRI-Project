"""agent.py"""

from agent.interactions import *
import re
import random
from colorama import init
from termcolor import colored

botName=colored('Sara','yellow')

class Agent:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener
        self.prezzo=0
        self.lista_=[]
        self.listaNum_=[]

        self.waitForFlowers= False
        self.trigger=False

    def think_man(self, command:str):
        varx=command.upper()
        match=find_match(self,varx)
        if match == '2':
            self.waitForFlowers = True
        if match == '4':     #tipologia evento
            varx2=command.split()
            db2_find(self,varx2) 
        if match== '5':
            varx2=command.split()
            price_fun(self,varx2)
        if match== '8':
            self.trigger=True
            trigger_request(self,command.split())
            self.lista_=[]
            self.listaNum_=[]
            self.prezzo=0
        if match==False:
            print(botName+colored(": Mi dispiace non abbiamo nulla",'red'))
            self.speaker.speak("Mi dispiace non abbiamo nulla")


def find_match(self,command):
    for k in Richieste:
        for i, interaction in enumerate(Richieste[k]):
            match = re.search(interaction.upper(),command)
            if self.waitForFlowers == True:
                varx2=command.split()
                self.waitForFlowers=False
                ownFlowers(self,varx2)
               
                return None
            if match:
                if  Risposte[k][0]!="" :
                    print(botName+": "+Risposte[k][0])
                    self.speaker.speak(Risposte[k])
                return k
    return False



def db2_find(self,varx2):
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



def price_fun(self,varx2):
    if self.prezzo==0:
        price=single_price(self,varx2)
        print(botName+": Il prezzo è di "+str(price)+" euro")
        pr="Il prezzo è di "+str(price)+" euro"
        self.speaker.speak(pr)
    else :
        pr="Il costo è di "+str(self.prezzo)+" euro"
        print(botName+": "+pr)
        self.speaker.speak(pr)
        self.prezzo=0

def single_price(self,varx2):
    for v in varx2:
        v2=v.capitalize()
        v2=v2[:-1]
        if v2 != '':   
            for vv in database:
                vv1=vv[:-1]
                vv2=vv[:-2]
                if v2 ==vv1 or v2 ==vv2:
                    return database[vv]


def ownFlowers(self,varx2):

    if self.trigger==False:
        self.lista_=[]
        self.listaNum_=[]
    for v in varx2:
        v2=v.capitalize()
        v2=v2[:-1]
        if v2 != '':   
            for vv in database:
                vv1=vv[:-1]
                vv2=vv[:-2]
                if v2 ==vv1 or v2 ==vv2:
                    if vv not in self.lista_:
                        self.lista_.append(v.lower())
    for v in varx2:
        
        if v.isnumeric():
            v=int(v)
            self.listaNum_.append(v)
        else:
            v=v.upper()
            for vv in database3.keys():
                vx=vv.upper()
                if v == vx:
                    self.listaNum_.append(database3[vv])
    if self.trigger==False:
        print_list(self)
    else:
        return 


def print_list(self):
    x=""
    if len(self.lista_)==len(self.listaNum_) and len(self.lista_)!=0:
        for elem in self.listaNum_:
            self.prezzo+=elem
        for elem in range(len(self.lista_)):
            x+=str(self.listaNum_[elem])+" "+self.lista_[elem]+" "
        fun="Perfetto, il suo mazzo sarà composto da: "+x
        print(botName+": "+fun)
        self.speaker.speak(fun)
    else:
        fun="Scusi non ho capito, potrebbe ripetere?"
        print(botName+": "+fun)
        self.speaker.speak(fun)
        self.waitForFlowers = True


def trigger_request(self,varx):
    ownFlowers(self,varx)
    if self.listaNum_==[]:
        fun="Quante ne mettiamo?"
        print(botName+": "+fun)
        self.speaker.speak("Quante ne mettiamo?")
        command,taken=self.listener.listen()
        ownFlowers(self,command.split())
        while len(self.listaNum_)!= len(self.lista_):
            fun="Scusi non ho capito quanti, potrebbe ripetere?"
            print(botName+": "+fun)
            self.speaker.speak("Scusi non ho capito quanti, potrebbe ripetere?")
            command,taken=self.listener.listen()
            ownFlowers(self,command.split())
    for i in range(len(self.lista_)):
        self.prezzo+=database[self.lista_[i]]*self.listaNum_[i]
    totale="Perfetto, il prezzo totale è di "+str(self.prezzo)+" euro"
    print(botName+": "+totale)
    self.speaker.speak(totale)
    
    self.trigger=False
