class Jeu:
    def __init__(self):
        self.personnages = []

    def ajouter(self, p):
        self.personnages.append(p)

    def retirer(self, p):
        self.personnages.remove(p)

    def afficher(self):
        for p in self.personnages:
            print(p)

    def tour(self):
        for p in self.personnages:
            if p.est_vivant():
                ennemis = [e for e in self.personnages if e != p and e.est_vivant()]
                if ennemis:
                    p.attaquer(ennemis[0])
class Personnage:
    def __init__(self, nom, sante, x, y, dimension):
        self.__nom = nom
        self.__sante = sante
        self.__position = (x, y)
        self.__dimension = dimension

    def deplacer(self, x, y):
        self.__position = (x, y)

    def subir_degats(self, degats):
        self.__sante -= degats
        print(f"{self.__nom} subit {degats} dégâts. Santé restante : {self.__sante}")

    def attaquer(self, autre):
        pass

    def get_nom(self):
        return self.__nom

    def get_position(self):
        return self.__position

    def est_vivant(self):
        return self.__sante > 0

    def __str__(self):
        return f"{self.__nom} - Santé: {self.__sante} | Pos: {self.__position}"
class Archer(Personnage):
    def __init__(self, nom, sante, x, y, dimension, precision):
        super().__init__(nom, sante, x, y, dimension)
        self.precision = precision

    def attaquer(self, autre):
        print(f"{self.get_nom()} tire une flèche !")
        autre.subir_degats(10)

class Dimension:
    def __init__(self, nom):
        self.nom = nom

class Guerrier(Personnage):
    def __init__(self, nom, sante, x, y, dimension, force):
        super().__init__(nom, sante, x, y, dimension)
        self.force = force

    def attaquer(self, autre):
        print(f"{self.get_nom()} attaque en guerrier !")
        autre.subir_degats(15)

class Magicien(Personnage):
    def __init__(self, nom, sante, x, y, dimension, puissance_sort):
        super().__init__(nom, sante, x, y, dimension)
        self.puissance_sort = puissance_sort

    def attaquer(self, autre):
        print(f"{self.get_nom()} lance un sort !")
        autre.subir_degats(12)

dim1 = Dimension("Forêt")
dim2 = Dimension("Montagne")

g = Guerrier("Thor", 100, 0, 0, dim1, 10)
m = Magicien("Merlin", 80, 1, 1, dim2, 20)
a = Archer("Legolas", 90, 2, 2, dim1, 0.9)

jeu = Jeu()
jeu.ajouter(g)
jeu.ajouter(m)
jeu.ajouter(a)

jeu.afficher()
for i in range(3):
    print(f"\n--- Tour {i+1} ---")
    jeu.tour()