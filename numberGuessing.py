'''
    File    : Number Guessing
    Author  : Programming The Universe
    Goal    : Program an Number Guessing algorithm. First, the user will choose a range (0 - 10, 0 - 50, 0 - 100) and
    then choose a number inside this range. If the number choosed is correct, the algorithm stops and prints that the
    choice is correct. If wrong, the algorithm would be able to give 3 clues and the user will choose again.
'''

'''
    operations() => Function that observe many info about the generated number.
    :param =>       
            - number = generated number
            - userRange = range from user choice
    :returns =>
            - tipList = list that contains some tips to help the user to find out the number
'''

# coding: utf-8

'''
    File    : Number Guessing
    Author  : Programming The Universe
    Goal    : Program an Number Guessing algorithm. First, the user will choose a range (0 - 10, 0 - 50, 0 - 100) and
    then choose a number inside this range. If the number choosed is correct, the algorithm stops and prints that the
    choice is correct. If wrong, the algorithm would be able to give 3 clues and the user will choose again.
'''

# Imports
import random, math

'''
    operations() => Function that observe many info about the generated number.
    :param =>       
            - number = generated number
            - userRange = range from user choice
    :returns =>
            - tipList = list that contains some tips to help the user to find out the number
'''


def operations(number, userRange):
    # VARIABLES
    # Var to define if the right number is (or not) a prime number
    ver = "is not"

    # List that contains the tips
    tipList = []

    # OPERATIONS
    # Verifying if the number is an even or odd number
    if (number % 2 == 0):
        tipList.append("The number is an even number.")
    else:
        tipList.append("The number is an odd number.")

    # Finding out the divisible number from the right number
    for x in range(2, number):

        if (number == 0):
            break

        if (number % x == 0):
            tipList.append("The number is divisible by {}.".format(x))

    # Verifying if the number is a prime number
    primeList = [2]
    for x in range(2, number + 1):

        for y in primeList:

            if (x % y == 0):
                break
        else:
            primeList.append(x)

    if (number in primeList):
        ver = "is"

    tipList.append("The number {} a prime number.".format(ver))

    # Setting up the min/max values ("the number is between varMin and varMax")
    varMin = random.random() * (number - 1)

    varMax = random.random() * userRange
    while (varMax <= number):
        varMax = random.random() * userRange
    tipList.append("The number is between {} and {}.".format(math.ceil(varMin), math.ceil(varMax)))

    # Verifying if the number is in the first or second half
    half = userRange // 2

    if (number < half):
        halfStr = "in first half."
    elif (number > half):
        halfStr = "in second half."
    else:
        halfStr = "neither in first half nor second half..."

    tipList.append("The number is {}".format(halfStr))

    return tipList


def main():
    print('''
    Hello, this is a funny Number Guess Game. Here you step-by-step to game:
    1: Type a max number equals or greater than 10 (the current range will be 0 to your enter);
    2: You receive your first tip randomically.
    3: You take your 1st shot.
    4: If right, the game will be over and you've won. Simple. If wrong, you receive the 2nd tip randomically.
    5: You take your 2nd shot.
    6: The 4th and 5th step repeats itself until the tips over.
    7: If you've not achieve the result, the tips over and you give you last shot.
    8: If right, you've won the game in the last attempt. If not... YOU'VE LOST !
    9: The info about the game is printed on the screen.

    GOOD LUCK !
    ''')

    # Input range
    userRange = int(input("Choose a max number (greater than 10) to your Number Guessing range: "))
    while (userRange < 10):
        print("The number must be greater than 10!")
        userRange = int(input("Choose a max number (greater than 10) to your Number Guessing range: "))

    # NUMBER TO BE FOUND OUT
    rand = random.random()
    number = int(userRange * rand)

    shots = []
    tipList = operations(number, userRange)
    tips = tipList.copy()

    # Controlling the shots...
    for i in range(len(tipList)):

        tip = random.choice(tipList)
        print("\nTip: {} Tips remaining: {}".format(tip, len(tipList)))
        tipList.remove(tip)

        shot = int(input("Give a shot: "))
        shots.append(shot)

        if (number in shots):
            print("\nYOU'VE WON !")
            break

    else:
        print("\nNice try but YOU'VE LOST !")

    # Printing the info
    print("\n\nRange: 0 - {}\nNumber: {}\nShots: {}".format(userRange, number, shots))

    for s in range(len(tips)):
        print("Tip {}: {}".format(s, tips[s]))


if __name__ == "__main__":
    main()
