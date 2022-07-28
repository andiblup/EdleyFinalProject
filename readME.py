 
    # INFORMATION - ERKLÄRUNG
    
	# Mein ursprünglicher plan war es ein objekt über ein dict mit key= artikelnummer und value als liste der restöichen attribute im sortiment zu appenden.
    # Leider hatte ich immer ein Problem mit dem referenzieren der objekte oder mit der Datenkapselung.
    # Also habe ich mehrere verschiedene herangehensweisen für dieses Projekt versucht.
    # Ich habe mich dann letztendlich doch dafür entschieden die Objekte nicht per Dictionary anzupeilen sondern als die Objekte die Sie sind.
    # Ein weitere Vorgehensweise um den Code einfacher zu halten war die Objektmanipulation nur über get und set Methoden durchzuführen und nicht wie in meinen ersten Exemplaren mit eigendefinierten Methoden.
    
    # Für die Artikelnummer habe ich entschieden das jede Nummer nicht nur einmal vorkommt sondern nur einmal im derzeitigen Sortiment.
    # Also das die Artikelnummer eines gelöschten Auto wieder vergeben wird.
    # Ich persönlich fand diese herangehensweise wesentlich professioneller als immer die letzte nummer plus Eins zu rechnen und dann einfach lücken in der Liste zu lassen.
    
    # Ich habe auch absichtlich kein os.clear() eingebaut, damit Sie die Schritte einfachnachverfolgen können. 
    # Stattdessen habe ich mich dafür entschieden Leerzeilen einzsetzen um etwas übersicht über alle Schritte zu bewahren.
     
    # Ich würde mich um ein Feedback von meinem Code sehr freuen, alleine schon um zu wissen wo ich derzeit stehe und auf welchen Bereich ich jetzt gerade noch mehr Fokus legen sollte
    # Über 60 Stunden habe ich verschiedenste Versionen dieses Programmes gemacht und versucht ein Programm zu machen mit dem ich zufrieden bin.
    # Ich habe meine Programmierkenntnisse im Laufe dieses Projektes sichtbar verbessert, vom ersten bis zu diesem Entwurf liegen in meinen Augen Welten.
    # Für mich war das schwerste an diesem Projekt die Ahnungslosigkeit ob ich wirklich die Anforderungen erfülle und ohne Rücksprache zu entscheiden das dieser Code gut genug ist. 
    
    # Mein Projekt besteht aus 3 Python Dateien und dieser README Datei, 
    # wobei diese README Datei für Sie nur als Übersicht und meinerseits als Kommunikationsmittel gedacht ist.
    # In autoClass.py befindet sich die Klasse Auto
    # In autoFunctions.py befinden sich die Funktionen und die main()-Funktion - autoClass wird importiert. 
    # In main.py befindet sich der main() Aufruf und ist somit das Hauptdokument - autoFunctions wird importiert  






# TODO: 1)
    ##########################################
    #   Endlosschleife
    #   Abfrage Aktion
    #
    #   Neuen Wagen hinzufügen
    #   Fahrzeug verkaufen
    #   Preis eines Fahrzeugs ändern
    #   Sortiment anzeigen
    #   Programm beenden
    ##########################################

"""
eventLoop = True

while eventLoop:
    
	question = input("Welche der folgenden Aktionen wollen Sie durchführen?\n1) Neuen Wagen hinzufügen\n2) Fahrzeug verkaufen\n3) Preis eines Fahrzeugs ändern\n4) Sortiment anzeigen\n5) Programm beenden\n")
    continue
"""  
        
# TODO: 2)
    ##########################################
    #   Jedes Auto in einem Objekt speichern
    #   neues Modul: Klasse Auto
    #   Enthaltene Attribute:
    #
    #   Artikelnummer
    #   Marke
    #   Modell
    #   Farbe
    #   Baujahr
    #   Preis
    ##########################################
    
"""
    class Auto:
        def __init__(self, artikelnummer, marke, modell, farbe, baujahr, preis):
    	self.__artikelnummer = artikelnummer
        self.__marke = marke
        self.__modell = modell
        self.__farbe = farbe
        self.__baujahr = baujahr
        self.__preis = preis
"""

# TODO: 3)
	##########################################
	# Für jede Aktion eine passende Methode 
	# oder Funktion erstellen.
	#
	# Zugriff auf Objekt - Methode
	# ansonsten Funktion
    ###########################################

# TODO: 4)
    ##########################################
	# Gesamtes Sortiment als Liste.
	# Diese enthällt die Auto Objekte.
	#
	# Zugriff auf Objekt über Artikelnummer 
    ###########################################
    
    # TODO drei und vier habe ich gleich gemiensam ererbeitet, um von Anfang an das Sortiment als Prüfliste zur Verfügung zu haben.
    # Außerdem weiß ich nicht wie ich eine Funktion schreiben soll in der ich etwas in einer Liste anhängen soll ohne vorher eine Liste gemacht zu haben.
    # Ich hoffe es war kein Fehler, nur möchte ich keine Funktion oder Methode schreiben die garnichts bewirkt.
    # Zudem  
    
    
    
    # FUNKTIONEN
"""
def print_out(object):
    print("ARTIKELNUMMER: ", object.getArtikelnummer(), " MARKE: ", object.getMarke(), " MODELL: ", object.getModell(), " FARBE: ", object.getFarbe(), " BAUJAHR: ", object.getBaujahr(), " PREIS: ", object.getPreis(), "\n")

def check_artikelnummer(artikelnummern):
    count = 0
    for each in artikelnummern:
        print(each)
        if count != each:   # if counter not in artikelnummer
            artikelnummer = count
            artikelnummern.insert(artikelnummer, count) 
            return artikelnummer
        else:
            count += 1
    return artikelnummern[-1] + 1

def append_car(artikelnummern, sortiment):
    marke = input("Welche Marke hat das Auto?\n")
    modell = input("Wie heißt das Modell?\n")
    farbe = input("Welche Farbe hat das Auto?\n")
    baujahr = int(input("Welches Baujahr hat das Auto?\n"))
    preis = float(input("Wie viel soll das Auto kosten? Ohne Euro zeichen.\n"))
    artikelnummer = check_artikelnummer(artikelnummern=artikelnummern)
    artikelnummern.append(artikelnummer)
            
    sortiment.append(Auto(artikelnummer, marke, modell, farbe, baujahr, preis))
    
    count = 0
    for object in sortiment:
        count += 1
        if object.getArtikelnummer() != count:
            a = sortiment[-1]
            b = sortiment[count - 1]
            sortiment.append(sortiment[count - 1])
            sortiment[count - 1] = sortiment[-2]
            del sortiment[-2]
    print("Der Prozess war erfolgreich und das Auto befindet sich nun im Sortiment.\n")

def show_sortiment(sortiment):
    inp = input('Bitte geben Sie "all" für das gesamte Sortiment oder die gewünschte Artikelnummer ein.\n').lower()
    if inp == "all":
        print("###########  GESAMTES SORTIMENT  ###########\n")
        for object in sortiment:
            print_out(object)
    else:
        for object in sortiment:
            if object.getArtikelnummer() == int(inp):
                print_out(object)

def sell_car(sortiment, artikelnummern):
    sellId = int(input("Wie lautet die Artikelnummer des zu verkaufenden Fahrzeuges?\n"))
    counter = 0
    for object in sortiment:
        counter += 1
        if object.getArtikelnummer() == sellId:
            print("Das verkaufte Objekt:\n ")
            print_out(object)
            print("wurde erfolgreich aus dem Sortiment genommen!\n")
            del sortiment[counter - 1]
            del artikelnummern[counter]
            continue

def change_price(sortiment):
    aNummer = int(input("Bitte geben Sie die Artikelnummer des zu verändernden Fahrzeuges ein.\n"))
    for object in sortiment:
        if object.getArtikelnummer() == aNummer:
            object.setPreis(float(input(" \nWie hoch ist der neue Preis?\n")))
            print(" \nHier sehen Sie den bearbeiteten Artikel:\n")
            print_out(object)

def exit_mainloop():
    return False




def main():
    # MAINLOOOP
    sortiment = []
    artikelnummern = [0]
    mainloop = True

    while mainloop:
        question = input("Welche der folgenden Aktionen wollen Sie durchführen?\n1) Neuen Wagen hinzufügen\n2) Fahrzeug verkaufen\n3) Preis eines Fahrzeugs ändern\n4) Sortiment anzeigen\n5) Programm beenden\n")
        
        if question == "1" or question == "Neuen Wagen hinzufügen" or question == "neuen wagen hinzufügen":
            append_car(artikelnummern=artikelnummern, sortiment=sortiment)
            continue
    
        elif question == "2" or question == "Fahrzeug verkaufen" or question == "fahrzeug verkaufen":
            sell_car(sortiment=sortiment, artikelnummern=artikelnummern)
            continue
        
        elif question == "3" or question == "Preis eines Fahrzeugs ändern" or question == "preis eines fahrzeugs ändern":
            change_price(sortiment=sortiment)
            continue
        
        elif question == "4" or question == "Sortiment anzeigen" or question == "sortiment anzeigen":
            show_sortiment(sortiment=sortiment)
            continue
        
        elif question == "5" or question == "Programm beenden" or question == "programm beenden":
            mainloop = exit_mainloop()
"""    

# METHODEN

"""
    # artikelnummer
    def getArtikelnummer(self):
        return self.__Artikelnummer

    def setArtikelnummer(self, artikelnummer):
        self.__Artikelnummer = artikelnummer
    
    # marke
    def getMarke(self):
        return self.__Marke

    def setMarke(self, marke):
        self.__Marke = marke
    
    # modell
    def getModell(self):
        return self.__Modell

    def setModell(self, modell):
        self.__Modell = modell
    
    # farbe
    def getFarbe(self):
        return self.__Farbe

    def setFarbe(self, farbe):
        self.__Farbe = farbe
    
    # baujahr
    def getBaujahr(self):
        return self.__Baujahr

    def setBaujahr(self, baujahr):
        self.__Baujahr = baujahr
    
    # preis
    def getPreis(self):
        return self.__Preis

    def setPreis(self, preis):
        self.__Preis = preis
"""


# main()












