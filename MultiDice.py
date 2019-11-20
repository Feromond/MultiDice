from random import *
import random
import time


while True:
    try:
        print("How many dice would you like to roll?(Blank line to quit)")
        numOfDice = int(input("Enter here: "))
    except ValueError:
        if numOfDice > 0:
            print("Enter a valid number of dice, or press enter to quit")
        else:
            print("Goodbye :)")
    if numOfDice == 0:
        break
    listOfValues = []
    Start_time = time.time()
    while numOfDice > 0:
        value = randint(1,6)
        numOfDice -= 1
        listOfValues.insert(0,value)
    #Add up values to get total roll value
    sumOfValues = sum(listOfValues)
    print("Total value of your roll is",sumOfValues)
    print("Run time is --- %.4f seconds ---" % (time.time() - Start_time))


