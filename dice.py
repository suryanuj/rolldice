#Created by Suryanuj Gupta. Made to practice python.
import random as dicenum

min=1
max=6

type=int(input("Do you want to:\n(1) Enter the amount of dice you want to roll first?\nOR\n(2) Roll one di at a time?\n\nEnter number: "))

if type ==1:
    number=input("How many dice do you want to roll? ")

    for i in range(int(number)):
        print("Rolling Dice...")
        print("You rolled a ", dicenum.randint(min, max))
        print("-------------------")

    exit()

elif type ==2:
    roll=True
    while roll or rollagain=="Yes" or rollagain=="yes":
        print("Rolling Di...")
        print("You rolled a",dicenum.randint(min,max))

        roll=False

        rollagain=input("\nDo you want to roll again (Y/N)? ")

        if rollagain == "Y":
            roll=True
        else:
            exit()
