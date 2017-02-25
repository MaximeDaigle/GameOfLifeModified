class Organisme:

    def __init__(self, type):
        self.type = type  #Couleur de l'organisme
        rules = open("rules.txt").readlines()
        for i in range(3):
            if type == rules[i][0]:
                abc = rules[i][2:].split(",")
                self.a = int(abc[0])  #Nombre de voisins pour que l'organisme naisse (nb v == a => nouvel organisme)
                self.b = int(abc[1])  #Nombre minimal de voisins pour que l'organisme reste vivant (nb v < b => meurt)
                self.c = int(abc[2])  #Nombre maximal de voisins pour que l'organisme reste vivant (nb v > c => meurt)
