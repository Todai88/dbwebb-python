"""
Marvin
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
import math


def meImage():
    """
    Store my ascii image in a separat variabel as a raw string
    """
    return r"""
                _______
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \
    """


def menu():
    """
    Display the menu with the options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(meImage())
    print("Welcome.\nMy name is Ragnar.\nWhat can I do for you?\n")
    print("1) Present yourself to Ragnar.")
    print("2) Have Ragnar calculate your minimum age (in seconds).")
    print("3) Have Ragnar calculate weight on the moon.")
    print("4) Try Ragnar's abilities by having him calculate minutes to hour(s).")
    print("5) Have Ragnar calculate Fahrenheit from Celcius.")
    print("6) See if Ragnar can multiply a word of your liking by a factor of your choice.")
    print("7) Have Ragnar print 10 numbers within a range of your choice.")
    print("8) Keep entering numbers and have Ragnar print their sum and average.")
    print("9) Let Ragnar calculate your grade by entering your score!.")
    print("10) Let Ragnar calculate the area of a circle with the radius of your choice.")
    print("11) Let Ragnar calculate the hypotenuse of a triangle with the sides of your choice.")
    print("12) Have Ragnar compare a given number to your previous number.")
    print("q) Quit.")


def myNameIs():
    """
    Read the users name and say hello to Marvin.
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")


def yearsToSec():
    """
    Calculate your age (years) to seconds
    """

    years = input("How many years are you?\n")
    seconds = int(years) * (365 * 24 * 60 * 60)
    print(str(years) + " would give you " + str(seconds) + " seconds.")
    return

def weightOnMoon():
    """
    Calculate your weight on the moon
    """

    weight = input("What is your weight (in kiloes)?\n")
    moonGrav = float(weight) * .2
    print(str(weight) + " kiloes would weigh be the same as " + str(moonGrav) + " kiloes on the moon.")

def minsToHours():
    """
    Calculate hours from minutes
    """

    minutes = input("How many minutes would you want to converted to hour(s)?\n")
    hours = float(format(float(minutes) / 60, '.2f'))
    print(str(minutes) + " hours is " + str(hours) + " hours")

def celToFahr():
    """
    Calculate celcius to Fahrenheit
    """

    cel = input("Please insert Celcius to be calculated to Fahrenheit.\n")
    fah = float(format(float(cel) * 1.8 + 32, '.2f'))
    print(str(cel) + " is " + str(fah) + " in Fahrenheit units.")

def multiplyWord():
    """
    Multiply word n-times
    """

    word = input("Please enter the word.\n")
    factor = input("And please give me the product to multiply it by!")
    word *= int(factor)
    print("The word is:\n" + str(word))

def randNumber():
    """
    Adds 10 random numbers (depending on user range)
    to a string.
    """

    rangeMin = input("What is the lower number in your range?\n")
    rangeMax = input("What is the higher number in your range?\n")
    sequence = ""
    for num in range(0, 10):
        sequence += str(randint(int(rangeMin), int(rangeMax))) + ", "
        num = num
    print("The random sequence is:\n" + sequence[:-2])

def sumAndAverage():
    """
    Adds numbers to the sum and calculate the average value of the input(s)
    """

    summa = 0
    count = 0
    temp = input("Please enter a number to be added to the sum. \nEnter 'q' if you wish to finish!\n")
    while True:
        if temp == "q":
            print("The sum of your numbers are: " + str(summa) + "\nAnd the average is: " + str(summa/count))
            return
        else:
            try:
                summa += int(temp)
                count += 1
                temp = input("Please enter a number to be added to the sum. \nEnter 'q' if you wish to finish!\n")
            except ValueError:
                print("That's not an int! \nPlease try again!")


def gradeFromPoints():
    """
    Shows the user's grade based on his / her points
    """
    maxPoints = input("What is the max score?\n")
    points = input("How many points did you score?\n")

    print("Your score: " + str(points) + "\nScore: {0}".format(float(maxPoints) * 0.5))
    if float(points) >= float(maxPoints) * 0.9:
        print("You got an A!")

    elif float(points) >= float(maxPoints) * 0.8 and float(points) < float(maxPoints) * 0.9:
        print("You got a B!")

    elif float(points) >= float(maxPoints) * 0.7 and float(points) < float(maxPoints) * 0.8:
        print("You got a C!")

    elif float(points) >= float(maxPoints) * 0.6 and float(points) < float(maxPoints) * 0.7:
        print("You got a D!")

    else:
        print("You failed the class")

def areaFromRadius():
    """
    Calculates a circles area based on it's radius
    """

    radius = input("What is the circle's radius?\n")
    area = (float(radius) * float(radius)) * 3.1416
    print("The area of the circle is: " + str(format(area, '.2f')))
    print("This was calculated with this formula: (radius^2) * 3.1416")

def calcHypotenuse():
    """
    Calculates a triangle's hypotenuse based on it's sides
    """
    side1 = input("How long is the first side?\n")
    side2 = input("How long is the second side?\n")
    hypotenuse = math.sqrt((float(side1) * float(side1)) + (float(side2) * float(side2)))
    print("The hypotenuse is: " + str(hypotenuse))

def compareNumbers(a, b):
    """
    Compares two numbers
    """
    if (a > b):
        print("Your previous number was larger!")
        return a
    elif (a < b):
        print("Your new number was larger!")
        return b
    else:
        print("They were equal!")
        return a

def validateInt(a):
    """
    Validates that an input is an integer
    """
    if a == 'q':
        return a
    else:
        flag = False
        while (flag == False):
            try:
                a = int(a)
                flag = True
            except ValueError:
                print("That's not an int! \nPlease try again!")
                a = input("Try again!\n")
    return a




def checkNumber(prev="first"):
    """
    Checks the number
    """
    print("\n=================\n")

    if prev == "first":
        prev = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        print("\n=================\n")
        new = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        if new == 'q' or prev == 'q':
            print("You have exited the loop\n")
            return
        else:
            compareNumbers(int(prev), int(new))
            checkNumber(str(new))
    else:
        new = validateInt(input("Please input a number. Press 'q' if you wish to end\n"))
        if new == 'q':
            print("You have exited the loop!\n")
            return
        else:
            compareNumbers(int(prev), int(new))
            checkNumber(str(new))



def main():
    """
    This is the main method, I call it main by convention.
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """

    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            return

        elif choice == "1":
            myNameIs()

        elif choice == "2":
            yearsToSec()

        elif choice == "3":
            weightOnMoon()

        elif choice == "4":
            minsToHours()

        elif choice == "5":
            celToFahr()

        elif choice == "6":
            multiplyWord()

        elif choice == "7":
            randNumber()

        elif choice == "8":
            sumAndAverage()

        elif choice == "9":
            gradeFromPoints()

        elif choice == "10":
            areaFromRadius()

        elif choice == "11":
            calcHypotenuse()

        elif choice == "12":
            checkNumber()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to continue...")



if __name__ == "__main__":
    main()
