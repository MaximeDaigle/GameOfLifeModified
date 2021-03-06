from grille import Grille
import sys

#Initialisaton de la grille
ficheInit = open("config.txt").readlines()
dimensionGrille = ficheInit[0][:-1].split(",")
grilleJeu = Grille(int(dimensionGrille[1]), int(dimensionGrille[0]))

#place les organismes initiales selon config.txt
grilleJeu.init(ficheInit)

try:
    parametre = sys.argv[1]
except IndexError:
    parametre = input("add a parameter")

#selectionne le bon mode d'execution
if parametre == 'animation':
    grilleJeu.afficherGrille()
    while True:
        input()
        for i in range(30):
            print('\n')
        grilleJeu = grilleJeu.actualisation()
        grilleJeu.afficherGrille()

elif parametre == 'couleur':
    grilleJeu.afficherGrilleCouleur()
    while True:
        input()
        for i in range(30):
            print('\n')
        grilleJeu = grilleJeu.actualisation()
        grilleJeu.afficherGrilleCouleur()

else:
    grilleJeu.afficherGrille()
    for i in range(int(parametre)):
        print('\n')
        grilleJeu = grilleJeu.actualisation()
        grilleJeu.afficherGrille()
