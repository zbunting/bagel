import random

GUESSES = 10

while (True):
    print("I am thinking of a 3-digit number. Try to guess what it is")
    print("Here are some clues:")
    print("When I say:     That means:")
    print("  Pico          One digit is correct but in the wrong position.")
    print("  Fermi         One digit is correct and in the right position.")
    print("  Bagels        No digit is correct.")

    num_guesses = 0
    rand_num = random.randint(100,999)
    stringified_num = str(rand_num)

    print("I have thought up a number.")
    print(f' You have {GUESSES} guesses to get it.')

    while(True):
        num_guesses += 1
        print(f'Guess #{num_guesses}')
        s = input("Enter your guess for the number here:")

        if s == stringified_num:
            print("You got it!")
            break

        guess_hints = []

        for i in range(len(s)):
            if stringified_num[i] == s[i]:
                guess_hints.append('Fermi')
            elif s[i] in stringified_num:
                guess_hints.append('Pico')

        if len(guess_hints) == 0:
            print("Bagels")
        else:
            feedback = ' '.join(guess_hints)
            print(feedback)

        if num_guesses == GUESSES:
            print("You used up all your guesses!")
            break

    still_playing = input("Type quit to quit or anything to play again!")
    if still_playing == "quit":
        break