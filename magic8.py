# Name: Chase Miller
#   Prog Purpose: This Magin 8-Ball code uses a Python tople since the
#   user does not have the ability to change the 8-ball answers.
#   However, the program could have used a python list instead of a tuple.
# Note: Tuples use parenthese; Lists use square braces.

import random
answers_8_ball = ( "As I see it, yes", "Ask again later",
    "Better not tell you now", "Cannot predict now",
    "Concentrate and ask again", "don't count on it",
    "It is certain", "It is  decidedly so",
    "Most likely", "My reply is no",
    "My sources say no", "Outlook good",
    "Signs point to yes", "Very doubtful",
    "Without a doubt", "Yes",
    "Yes definitely", "You may rely on it",)

def main():

    print ("I am the MAGIC-8 BALL and can answer any YES or NO questions!")

    another_question = True
    while another_question:
        answer = random.choice (answers_8_ball )

        print("\nshake the MAGIC-8 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("The MAGIC-* ball says: " + answer)

        askAgain = input ("\nWould you like to ask me another question (Yor N)?: " )
        if askAgain.upper () == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions.")
    print("...MAGIC-8 Ball OUT.")

main()
