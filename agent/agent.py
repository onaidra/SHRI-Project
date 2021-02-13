"""agent.py"""

from agent.kb import *
import re
import random
from colorama import init
from termcolor import colored
import os
botName=colored('Sara','yellow')

def notFound(self,parole):
    #parole=["Non ti scordar di me","non ti scordar di me","Bocca di leone","Bocche di leone","Bocca di luna","Bocche di luna","Stella alpina","Stelle alpine"]
    with open("agent/general_db.txt","r") as f:
        linea=f.readline().strip("\n")
        while(linea):
            for p in parole:
                if p in linea:
                    if linea not in self.notFound and linea not in self.lista_:
                        self.notFound.append(linea)
            linea=f.readline().strip("\n")

    for i in range(len(self.lista_)):
        if self.lista_[i] in self.notFound:
            self.notFound.remove(self.lista_[i])

class Agent:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener
        self.prezzo=0
        self.lista_=[]
        self.listaNum_=[]
        self.notFound=[]
        self.nomi=[]
        self.colori=[]

        self.waitForFlowers= False
        self.trigger=False

    def think_man(self, command:str):
        varx=command.upper()
        print(self.trigger)
        match=find_match(self,varx)
        print(match)
        if match == '2':
            self.waitForFlowers = True
        if match == '4':     #tipologia evento
            varx2=command.split()
            db2_find(self,varx2) 
        if match== '5':
            varx2=command.split()
            price_fun(self,varx2)
            self.lista_=[]
            self.listaNum_=[]
            self.notFound=[]
            self.nomi=[]
            self.colori=[]
        if match == '8':
            self.trigger=True
            trigger_request(self,command.split())
            self.lista_=[]
            self.listaNum_=[]
            self.notFound=[]
            self.nomi=[]
            self.colori=[]

            self.prezzo=0
        if match == '9':
            self.trigger=True
            ownFlowers(self,command.split())
            self.trigger=False
            if(len(self.lista_)!=0):
                fun="Si le abbiamo e vengono rispettivamente "
                for i in range(len(self.lista_)):
                    if i<len(self.lista_)-1:
                        fun+=str(database[self.lista_[i]])+" euro e "
                    else:
                        fun+=str(database[self.lista_[i]])+" euro"
                print(botName+": "+fun)
                self.speaker.speak(fun)
                
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



def price_fun(self,varx2):  #controllo e calcolo il prezzo delle richieste
    if(len(self.lista_)!=0):        #se ho già inserito elementi calcolo il prezzo finale
        total_price(self)
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

def single_price(self,varx2):       #cerco il prezzo del singolo prodotto
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
    indexN=0
    
    if self.trigger==False:
        self.lista_=[]
        self.listaNum_=[]
        self.nomi=[]
        self.colori=[]
    for v in varx2:
        v2=v.capitalize()
        v2=v2[:-1]
        if v2 != '':   
            for vv in database:
                vv1=vv[:-1]
                vv2=vv[:-2]
                
                if v2 ==vv1 or v2 ==vv2:
                    if self.trigger==True:
                        if vv not in self.lista_:
                            self.lista_.append(vv)
                            self.nomi.append(v.lower())
                    else:
                        self.lista_.append(vv)
                        self.nomi.append(v.lower())
                    indexN+=1
                else:
                    if(v2[:-1]!=''):
                        notFound(self,[v2.capitalize()])
            for col in database4:
                col1=col[:-1].capitalize()
                if col1==v2:
                    if indexN>(len(self.colori)+1):
                        while indexN!=(len(self.colori)+1):
                            self.colori.append("")
                    if indexN==(len(self.colori)+1):
                        self.colori.append(v.lower())
       
    if indexN>len(self.colori):
        while indexN>len(self.colori):
            self.colori.append("")
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


def print_list(self):   #stampo la composizione del mazzo
    x=""
    if len(self.lista_)==len(self.listaNum_) and len(self.lista_)!=0:

        for elem in range(len(self.lista_)):
            if elem<1:
                x+=str(self.listaNum_[elem])+" "+self.nomi[elem]+" "+self.colori[elem]+" "
            else :
                x+="e "+str(self.listaNum_[elem])+" "+self.nomi[elem]+" "+self.colori[elem]+" "
        fun="Perfetto, il suo mazzo sarà composto da: "+x
        print(botName+": "+fun)
        self.speaker.speak(fun)
    
    else:
        if len(self.notFound)!=0:
            print_notfound(self)
            self.waitForFlowers = True
        else:
            fun="Scusi non ho capito, potrebbe ripetere?"
            print(botName+": "+fun)
            self.speaker.speak(fun)
            self.waitForFlowers = True

def total_price(self):  #calcolo prezzo totale finale
    for i in range(len(self.lista_)):
        self.prezzo+=database[self.lista_[i]]*self.listaNum_[i]

def print_notfound(self):
    fun=("Mi dispiace ma non abbiamo alcun ")
    
    if len(self.notFound)==1:
        fun+=self.notFound[0]
    
    else:
    
        for i in range(len(self.notFound)):
            if i<len(self.notFound)-1:
                fun+=self.notFound[i]+" ne "
            else:
                fun+=self.notFound[i]
    
    print(botName+": "+fun)
    self.speaker.speak(fun)
    self.trigger=False

def trigger_request(self,varx): #creo un mazzo da 0
    ownFlowers(self,varx)

    if self.notFound!=[]:       #fiori non presenti
        print_notfound(self)
        return
        
    if self.lista_==[]:         #nessun tipo di fiori
        self.trigger=False
        print_list(self)
        return
    
    if self.listaNum_==[]:
    
        fun="Quante ne mettiamo?"
        print(botName+": "+fun)
        self.speaker.speak("Quante ne mettiamo?")
    
        command,taken=self.listener.listen()
        ownFlowers(self,command.split())
    
        while len(self.listaNum_)!= len(self.lista_):
            print(self.lista_)
            print(self.listaNum_)
            fun="Scusi non ho capito quanti, potrebbe ripetere?"
            print(botName+": "+fun)
            self.speaker.speak("Scusi non ho capito quanti, potrebbe ripetere?")
            self.listaNum_=[]
            command,taken=self.listener.listen()
            ownFlowers(self,command.split())
    
    total_price(self)
    print_list(self)
    totale="Il prezzo totale è di "+str(self.prezzo)+" euro"
    print(botName+": "+totale)
    self.speaker.speak(totale)
    self.trigger=False
