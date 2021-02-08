"""agent.py
"""
import re
import random
database =  {"Rosa":3.5, "Calla":1.5, "Tulipano":3, "Giglio":3, "Gerbera":1.20, "Margherita":1, "Orchidea":7, "Girasole":4, "Viola":2, "Papavero":0.50,"Fiore di Loto":4,
"Ginestra":0.2, "Crisantemo":0.7, "arancio":0.3,  "Firdaliso":2.5, "Calendula":1, "Lavanda":0.3, "Non ti scordar di me":0.2, "Ortensia":2, "Peonia":1.5, "Mimosa":3,"Giacinti":8,
"Narcisi":1,"Ibisco":1.3,"Magnolie":1.2,"Pesco":0.3, "Acacia":0.3, "Azalea":1, "Anemone":1, "Gelsomino":0.2, "Erica":0.3,  "Iris":1.5, "Ciclamini":0.6, "Sterlitzia":2,"lillà":1,
"Zimnia":1.5,"Bocche di Leone":1,"Eucalipto":0.6,"Amaryllis":1.6,"Fresie":1 }
#print(database["Eucalipto"])

class Agent:
    def __init__(self, speaker, listener):
        self.speaker = speaker
        self.listener = listener

    def think_man(self, command):
        print(database[command])

	
