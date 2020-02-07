from donnees import *
from random import randrange

def entrerLettre():

    lettre = ""
    while len(lettre) != 1 or not lettre.isalpha() :
        try :
            print("donne une lettre :")
            lettre=input()
        except TypeError :
            print("une lettre")
        except ValueError :
            print("donne une lettre")
    return lettre

def remplaceLettre (motListeLettres,motADeviner, lettre) :

    for idLettre in range(len (motADeviner)) :
        if motADeviner[idLettre] == lettre.lower() :
            if motListeLettres[idLettre] == "*" :
                motListeLettres[idLettre] = lettre.lower()


continuerPartie = True
perdu = False
longeurTotaleMots = len(listeMots)

scoreJoueur = 0
print("Bienvenue au jeu du pendu, pour aller de l'ava... euh PARCE QUE C'EST NOTRE PROJEEEEEEEEET ! ! !")

while continuerPartie :
    print("Et c'est parti pour un nouveau mot a deviner !")
    nbChances = 8
    nombreHasard = randrange(longeurTotaleMots)
    motADeviner = listeMots[nombreHasard]

    longueurUnMot = len(motADeviner)
    motEtoiles = ["*"] * longueurUnMot
    
    motAffiche = "".join(motEtoiles)

    lettresDejaJouees = []

    while motADeviner != motAffiche and not perdu :
        
        motListeLettres = []
        for uneLettre in motAffiche :
            motListeLettres.append(uneLettre)

        lettre = entrerLettre()

        if lettre in motADeviner :
            remplaceLettre (motListeLettres,motADeviner, lettre)

        else :
            nbChances -=1
        lettresDejaJouees.append(lettre)
  
        if nbChances <= 0 :
            continuerPartie = False
            perdu = True
        
        motAffiche  = "".join(motListeLettres)

        print("ton mot : {}".format(motAffiche))
        print("nombre de chances : {}".format(nbChances))
        print("lettres deja jouees :")
        for dejajoue in range(len(lettresDejaJouees)) :
            print(lettresDejaJouees[dejajoue], end=" ")
        print()

    if not perdu :
        print("Félicitations ! tu as trouvé le mot magique : {}".format(motADeviner))
        scoreJoueur += nbChances
        continuer = input("Est-ce que tu veux arreter ? (o/n)")

        if continuer =="o" or continuer == "O" :
            continuerPartie = False

if perdu :
    print("C'est trop dommage ! Tu as perdu")
print("ton score est de {} points !".format(scoreJoueur))
print("Au revoir et à bientôt !")
