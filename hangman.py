from donnees import *
from random import randrange
from fonctions import *
import os

totalScores = loading_scores()

# " IMPLEMENTONS LE FAIT QUE TANT QUE C'EST LA MEME PARTIE ON NE DEMANDE PAS A CHAQUE FOIS LE NOM"

# implementer le fait qu'il ne doit jamais pondre le même mot 2 fois dans une même partie
gameOn = True
gameOver = False
totalNumberOfWords = len(listeMots)

print("Bienvenue au jeu du pendu ! !")

while gameOn :
    nbChances = nombreChances

    playerName = "#"
    while not playerName.isalnum() :
        playerName = input("Comment tu t'appelles ? \n")

    if playerName in totalScores :
        scorePlayer = totalScores[playerName]
    else :
        totalScores[playerName] = 0
        scorePlayer = 0

    randomNumber = randrange(totalNumberOfWords)
    wordToGuess = listeMots[randomNumber]

    lenghtOfWord = len(wordToGuess)
    hiddenWord = ["*"] * lenghtOfWord
    hiddenWord[0] = wordToGuess[0]
    hiddenWord[lenghtOfWord-1] = wordToGuess[lenghtOfWord-1]
    displayedWord = "".join(hiddenWord)

    playedLetters = []
    print("Et c'est parti pour un nouveau mot a deviner ! \n  {}".format(displayedWord))

    while wordToGuess != displayedWord and not gameOver :

        motListeletters = []
        for oneLetter in displayedWord :
            motListeletters.append(oneLetter)

        letter = entrerLettre()

        if letter in wordToGuess :
            replaceLetter (motListeletters,wordToGuess, letter)

        else :
            nbChances -=1
        playedLetters.append(letter)
  
        if nbChances <= 0 :
            gameOver = True
        if gameOver :
            continue = False

        displayedWord  = "".join(motListeletters)

        displayingWordScore(displayedWord, nbChances, playedLetters)

    if not gameOver :
        print("Félicitations ! tu as trouvé le mot magique : {}".format(wordToGuess))
        scorePlayer += nbChances
        totalScores[playerName] =scorePlayer

        print("Ton score actuel : {}".format(scorePlayer))
        continuer = input("Est-ce que tu veux arreter ? (o/n)")
        if continuer =="o" or continuer == "O" :
            gameOn = False

if gameOver :
    print("C'est trop dommage ! Tu as perdu")
    print_scores(totalScores)

recording_scores(totalScores)

print_scores(totalScores)
