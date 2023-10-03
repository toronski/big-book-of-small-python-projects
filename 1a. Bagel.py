# Bajgle by dmft

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("\nWelcome to the world of the Anglo-Saxon game 'Bagels'.\n I have a certain number in mind...\nCan you guess what the number is?")
    print("\nYou have {} attempts.".format(MAX_GUESSES))
    
    while True:
        print("\nLet's begin!")
        secret_Number = get_secret_Num()
        print(secret_Number)

        attempt = 1
        while attempt < MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS:
                guess = input("\nAttempt {}\n> ".format(attempt))
            
            print(clues(guess, secret_Number))
            attempt += 1
    
            if guess == secret_Number:
                break
            if attempt > MAX_GUESSES:
                print("\nYou used all your attempts... ")

        print("\nDO you want to play again (yes or no)?")
        if not input (' > ').lower().startswith('y'):
            break
        print("Thank you for playing.")


def get_secret_Num():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number

def clues(guess, secret_Number):

    if guess == secret_Number:
        return "Great success!"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_Number[i]:
            clues.append("FERMI")
        elif guess[i] in secret_Number:
            clues.append("PIKO")
    if len(clues) == 0:
        clues.append('BAGEL')
    clues.sort()
    return clues


if __name__ == "__main__":
    main()