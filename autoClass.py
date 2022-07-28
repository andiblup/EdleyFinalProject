
class Auto:
    
    def __init__(self, artikelnummer, marke, modell, farbe, baujahr, preis):
        self.__Artikelnummer = artikelnummer
        self.__Marke = marke
        self.__Modell = modell
        self.__Farbe = farbe
        self.__Baujahr = baujahr
        self.__Preis = preis
        
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
