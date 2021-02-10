"""interactions.py
"""
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

database3={'uno':1,'due':2,'tre':3,'quattro':4,'cinque':5,'sei':6,'sette':7,'otto':8,'nome':9,'dieci':10,'undici':11,'dodici':12,'tredici':13,'quattordici':14,
'quindici':15,'sedici':16,'diciasette':17,'diciotto':18,'diciannove':19,'venti':20,'ventuno':21,'ventidue':22,
'trenta':30,'quaranta':40,'cinquanta':50,'sessanta':60,'settanta':70,'ottanta':80,'novanta':90,'cento':100 }


Richieste = {
    '1': ["([a-z])?(Mi servirebbe|Vorrei|Ho bisogno di|Desidero|Voglio|Mi serve|Vorrei comprare|Voglio comprare|Desidero comprare)? un mazzo di fiori([a-z])?"],
    '2': ["([a-z])?(Ho qualche idea|Sì ho un'idea|Sì avevo un'idea|Sì un'idea|Sì ha un'idea)([a-z])?"],
    '3': ["([a-z])?(Mi consigli lei|Faccia lei|consiglio|non saprei|non ho idea|non ne ho idea|mi aiuti|mi consigli|fai tu|non so)([a-z])?"],
    '4': ["([a-z])?(matrimonio|compleanno|comunione|san valentino|funerale|festa della donna|anniversario|battesimo|fidanzamento)([a-z])?"],
    '5': ["([a-z])?(prezzo|costa|viene|costo|a quanto)([a-z])?"],
    '6': ["([a-z])?(lo prendo|va bene|perfetto|ok)([a-z])?"],
    '7': ["([a-z])?(altri|altro|diverso|diversi)([a-z])?"],
    '8': ["([a-z])?(mazzo di|mazzetto di)([a-z])?"],

    #'saluto': ["([a-z])?(arrivederci|ciao|alla prossima)([a-z])?"]

}

Risposte = {
    '1': ["Ha qualche idea o le posso consigliare io?"],
    '2': ["Con cosa vuole comporre il mazzo?"],
    '3': ["Per quale occasione è?"],
    '4': ["Ok, ho proprio qualcosa che fa per lei!"],
    '5': [""],
    '6': ["Ecco a lei il mazzo, arrivederla"],
    '7': ["No mi spiace, è l'unico che abbiamo per quel tipo di occasione"],
    '8': [""],
    'fiori':[]
    #'saluto': ["Arrivederci"]
}
