class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def set_y(self, y):
        self._y = y
    def set_x(self, x):
        self._x = x

    def __str__(self):
        return f"(x, y) = ({self._x}, {self._y})"

class Rectangle(Point):
    def __init__(self, x, y, longueur, largeur):
        super().__init__(x, y)
        self._longueur = longueur
        self._largeur = largeur
    
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur
    
    def set_longueur(self, longueur):
        self._longueur = longueur

    def set_largeur(self, largeur):
        self._largeur = largeur
    
    def aire(self):
        return (self._largeur * self._longueur)

    def __str__(self):
        return f"les coordonnees du coin doit-gauche ({super().get__x()}, {super().get__y()}),  la longueur est : {self._longueur}, la largeur est : {self._largeur} et la surface est : {self.aire()}"

class Parallelepipede(Rectangle):
    def __init__(self, x, y, longueur, largeur, hauteur):
        super().__init__(x, y, longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    
    def aire(self):
        return 2 * (super().get_longueur() * super().get_largeur() + super().get_longueur() * self.__hauteur + super().get_largeur() * self.__hauteur)

    def volume(self):
        return super().get_longueur() * super().get_largeur() * self.__hauteur
    
    def __str__(self):
        return f"le coin doit-gauche est : ({super().get_x(), super().get_y()}), la longueur de la base est : {super().get_longueur()}, la largeur de la base est : {super().get_largeur()}, la surface est : {self.aire()}, et le volume est : {self.volume()}"


p = Parallelepipede(1, 1, 1, 1, 1)

print(p)

        