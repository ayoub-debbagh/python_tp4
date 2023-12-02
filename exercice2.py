class Batiment:
    def __init__(self, adresse):
        self._adresse = adresse

    def get_adresse(self):
        return self._adresse

    def set_adresse(self, adresse):
        self._adresse = adresse

    def __str__(self):
        return f"L'adresse du batiment est {self._adresse}"


class Maison(Batiment):
    def __init__(self, adresse, nbPieces):
        super().__init__(adresse)
        self._nbPieces = nbPieces

    def get_nbPieces(self):
        return self._nbPieces

    def set_nbPieces(self, nbPieces):
        self._nbPieces = nbPieces

    def __str__(self):
        return f"L'adresse de la maison est : {self.get_adresse()}, nombre de pieces est {self._nbPieces}"


class Immeuble(Batiment):
    def __init__(self, adresse, nbAppart):
        super().__init__(adresse)
        self._nbAppart = nbAppart

    def get_nbAppart(self):
        return self._nbAppart

    def set_nbAppart(self, nbAppart):
        self._nbAppart = nbAppart

    def __str__(self):
        return f"L'adresse d'immeuble est {self.get_adresse()} et le nombre d'appartements est {self._nbAppart}"




maison = Maison("63 rue 12 nouvelle cite", 10)
print(maison)

immeuble = Immeuble("centre ville", 20)
print(immeuble)
