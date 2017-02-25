from Cellule import Cellule
from Organisme import Organisme
import copy

class Grille:

    def __init__(self, sizey, sizex):
        """
        :param sizey: nombre de ranger (int)
        :param sizex: nombre de colonne (int)
        """
        self.y = sizey
        self.x = sizex
        cell = []
        contenu = Cellule()
        for i in range(sizey):
            cellcol = []
            for j in range(sizex):
                cellcol.append(contenu)
            cell.append(cellcol)
        self.cell = cell

    def __getitem__(self, i):
        return self.cell[i]

    def init(self, ficheInit):
        """
        place les organismes initiales selon config.txt
        :param ranger: int
        :param colonne: int
        :param type: string
        """
        for i in ficheInit:
            if "\n" in i:
                cRC = i[:-1].split(",")  # liste contenant ["couleur","Range","Colonne"]
            else:
                cRC = i.split(",")
            if len(cRC) != 3:
                continue
            self.set(int(cRC[1]), int(cRC[2]), cRC[0])

    def afficherGrille(self):
        for i in range(self.y):
            ligne = ""
            for j in range(self.x):
                if self.cell[i][j].contenu == "None":
                    ligne += ". "
                elif self.cell[i][j].contenu.type == "R":
                    ligne += "R "
                elif self.cell[i][j].contenu.type == "B":
                    ligne += "B "
                elif self.cell[i][j].contenu.type == "G":
                    ligne += "G "
            print(ligne)

    def afficherGrilleCouleur(self):
        """
        affichage de la grille avec couleur
        :param ranger: int
        :param colonne: int
        :param type: string
        """
        for i in range(self.y):
            ligne = ""
            for j in range(self.x):
                if self.cell[i][j].contenu == "None":
                    ligne += ". "
                elif self.cell[i][j].contenu.type == "R":
                    ligne += '\033[91m' + '# ' + '\033[0m'
                elif self.cell[i][j].contenu.type == "B":
                    ligne += '\033[94m' + '# ' + '\033[0m'
                elif self.cell[i][j].contenu.type == "G":
                    ligne += '\033[92m' + '# '+ '\033[0m'
            print(ligne)

    def set(self,ranger,colonne,type):
        """
        place un organisme de type 'type' dans la cellule ranger,colonne
        :param ranger: int
        :param colonne: int
        :param type: string
        """
        self[ranger][colonne] = Cellule(Organisme(type))

    def meurt(self,ranger,colonne):
        """
        enleve un organisme qui meurt dans la cellule ranger,colonne
        :param ranger: int
        :param colonne: int
        """
        self[ranger][colonne] = Cellule()

    def actualisation(self):
        """
        Retourne une nouvelle grille avec les morts et naissance actualiser
        :return voisins: list
        """
        newGrille = copy.deepcopy(self)
        for i in range(self.y):
            for j in range(self.x):
                #actualise les naissances
                if self[i][j].contenu == "None":
                    checkN = self.check4naissance(i,j)
                    if checkN[0]:
                      newGrille.set(i,j,checkN[1])
                #actualise les morts
                else:
                    if self.check4mort(i,j):
                        newGrille.meurt(i,j)
        return newGrille

    def findVoisins(self, ranger , colonne):
        """
        Retourne une liste des types des voisins de la cellule situer a la colonne j, ranger i
        :param ranger: int
        :param colonne: int
        :return voisins: list
        """
        voisins = []
        for i in range(-1,2):
            for j in range(-1,2):

                # ignorer les coordonnees en dehors de la grille et la coordonnee de la cellule elle-meme
                if (ranger + i) < 0 or (ranger + i) > (self.y -1) or (colonne + j) < 0 or (colonne + j) > (self.x -1) or (i==0 and j==0): #passer les coordonnees en dehors de la grille
                    continue
                if self[ranger + i][colonne + j].contenu != "None":   #si il y a un organisme dans la cellule
                    voisins.append(self[ranger + i][colonne + j].contenu.type)
        return voisins

    def check4naissance(self, ranger, colonne):
        """
        Verifie s'il y a une naissance a la cellule situer a colonne,ranger
        Retourne une liste.
        le premier element est un boolean qui dit s'il y a naissance
        Si le premier element est true, le deuxieme element est la couleur de l'organisme qui nait
        :param ranger: int
        :param colonne: int
        :return result: list[boolean, 'string']
        """
        voisins = self.findVoisins(ranger, colonne)
        #Verifie s'il y a naissance et si oui de quelle couleur
        if len(voisins) == Organisme('R').a:
            return [True, 'R']
        elif len(voisins) == Organisme('G').a:
            return [True, 'G']
        elif len(voisins) == Organisme('B').a:
            return [True, 'B']
        else: return [False, "None"]

    def check4mort(self, ranger, colonne):
        """
        Verifie s'il y a un mort a la cellule situer a ranger, colonne
        :param ranger: int
        :param colonne: int
        :return boolean
        """
        voisins = self.findVoisins(ranger, colonne)
        org = self[ranger][colonne].contenu  #l'organisme a checker
        # Verifie s'il meurt
        if len(voisins) < org.b or len(voisins) > org.c:
            return True
        else:
            return False
