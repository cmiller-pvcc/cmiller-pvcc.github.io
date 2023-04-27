#Name: Chase-Miller
#Prog-Purpose: Pordle (PVCC Worlde)

import random

wordList = []
inFile = "animals.txt"
wordFile = None

def main():
    global wordList, wordFile
    playAgain = True
    while playAgain:
        printMenu()
        wordFile = open(inFile, "r")
        for textLine in wordFile:
            for word in textLine.split():
                wordList.append(word)
        wordFile.close()

        printHeadings()
        playGame()
 
        yesno = input("Would you like to play again? (Y/N) ")
        if yesno == "n" or yesno == "N":
            playAgain = False
            print ("Thank you for playing PORDLE!")
            return

def printHeadings():
    print("\nWelcome to PORDLE! The PVCC Wordle Game")
    print("I will think of a word and you try to guess the letters in the word.")
    print("The number of dashes indicates the number of letters in the word.")
    print("\nGet ready for a new word...")

def printMenu():
    global inFile
    print("\nChoose a PORDLE category:")
    print("\t1. Animals")
    print("\t2. Foods")
    print("\t3. Cars")
    print("\t4. Sports")
    category = input("Please enter the category number: ")

    if category == "1":
        inFile = 'animals.txt'
    elif category == "2":
        inFile = 'foods.txt'
    elif category == "3":
        inFile = 'cars.txt'
    elif category == "4":
        inFile = 'sports.txt'
    else:
        infile = 'animals.txt'
        print("This will be an ANIMAL pordle")

    wordFile = open(inFile, "r")  
    wordList.clear()
    for textLine in wordFile:
        for word in textLine.split():
            wordList.append(word)
    wordFile.close()

def playGame():
    numguesses = 0
    lettersUsed = []

    wordChosen = random.choice(wordList)
    pordle = '_' * len(wordChosen)
    print (" ".join(pordle))

    while pordle != wordChosen:
        letterGuess = input("Please enter a letter: ")
        letterGuess = letterGuess.lower()
        lettersUsed.append(letterGuess)
        print ("Number of guesses: " + str(numguesses))

        for i in range(len(wordChosen)):
            if wordChosen[i] == letterGuess:
                pordle = pordle[0:i] + letterGuess + pordle[i+1:]

        print("Used letters: ")
        print(lettersUsed)
        print(" ".join(pordle))
        numguesses += 1

    print("Well done! You guessed in " + str(numguesses-1) + " guesses!")

main()
