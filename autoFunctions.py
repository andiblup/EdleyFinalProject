
from autoClass import Auto

# FUNKTIONEN

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
