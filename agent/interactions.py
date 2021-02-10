"""interactions.py
"""

Richieste = {
    '1': ["([a-z])?(Mi servirebbe|Vorrei|Ho bisogno di|Desidero|Voglio|Mi serve|Vorrei comprare|Voglio comprare|Desidero comprare)? un mazzo di fiori([a-z])?"],
    '2': ["([a-z])?(Ho qualche idea|Sì ho un'idea|Sì avevo un'idea|Sì un'idea|Sì ha un'idea)([a-z])?"],
    '3': ["([a-z])?(Mi consigli lei|Faccia lei|consiglio|non saprei|non ho idea|non ne ho idea|mi aiuti|mi consigli|fai tu|non so)([a-z])?"],
    '4': ["([a-z])?(matrimonio|compleanno|comunione|san valentino|funerale|festa della donna|anniversario|battesimo|fidanzamento)([a-z])?"],
    '5': ["([a-z])?(prezzo|costa|viene|costo|a quanto)([a-z])?"],
    '6': ["([a-z])?(lo prendo|va bene|perfetto|ok)([a-z])?"],
    '7': ["([a-z])?(altri|altro|diverso|diversi)([a-z])?"],

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
    'fiori':[]
    #'saluto': ["Arrivederci"]
}
