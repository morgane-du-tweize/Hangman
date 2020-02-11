import os
import pickle

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

def replaceLetter (totalLetters,word, lettre) :
    for idLettre in range(len (word)) :
        if word[idLettre] == lettre.lower() :
            if totalLetters[idLettre] == "*" :
                totalLetters[idLettre] = lettre.lower()

def displayingWordScore(word, nbChances, lettes) :
    print("ton mot : {}".format(word))
    print("nombre de chances : {}".format(nbChances))
    print("lettres deja jouees :")
    for dejajoue in range(len(lettes)) :
        print(lettes[dejajoue], end=" ")
    print()

def afficheFelicitations(word, score , nbChances) :
    continuerPartie = True
    print("Félicitations ! tu as trouvé le mot magique : {}".format(word))
    score += nbChances
    continuer = input("Est-ce que tu veux arreter ? (o/n)")
    if continuer =="o" or continuer == "O" :
        continuerPartie = False
    return continuerPartie

def loading_scores() :
    if os.path.exists ("score.txt") :
        with open('score.txt', 'rb') as fichier :
            mon_depickler = pickle.Unpickler(fichier)
            scores = mon_depickler.load()
    else :
            scores = dict()
    return scores

def recording_scores(scores) :
    with open ('score.txt', 'wb') as fichier :
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(scores)

def print_scores(scores) :
    for idJoueur in scores :
        print("joueur : {}".format(idJoueur))
        print("score : {}".format(scores[idJoueur]))

if __name__ == "__main__" :
    lettreTayst = entrerLettre()
    print("tayst")
