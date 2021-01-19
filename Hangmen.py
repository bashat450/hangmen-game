import random
def hangman():

    word = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 3
    guessmade = ''

    while len(word) > 0:
        main = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!")
            break

        print("Guess the word:" , main)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character : ")
            guess = input()

        if guess not in word:
            turns = turns - 1
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break


name = input("Enter your name : ")
print("Welcome" , name )
print("-------------------")
print("try to guess the word in less than 3 attempts")
hangman()
print()
