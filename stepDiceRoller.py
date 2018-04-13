"""
Step Dice Roller
    by R. G. Blaine on 4/12/2018

calculates and rolls exploding dice for the step input by the user
"""

# imports
import random

# global variable
global PRINT_DEBUG
PRINT_DEBUG = True

################################################################################

def diceStep(step):

    '''
    calculates dice for the given step

    arguments
        step : non-negative integer

    output
        error message if step is not a non-negative integer

    returns
        tuple of 5 non-negative integers (the number of each die in the step)
    '''
    
    if (step < 0) or (step != abs(step)):
        print("\n\n\n !!! ERROR: Step must be a non-negative integer !!!\n\n\n")
        quit()

    # number of each die
    d4  = 0
    d6  = 0
    d8  = 0
    d10 = 0
    d12 = 0

    if step == 0:
        return (d12, d10, d8, d6, d4)
    elif step == 1:
        d4 += 1
    elif step == 2:
        d6 += 1
    elif step == 3:
        d8 += 1
    elif step == 4:
        d10 += 1
    elif step == 5:
        d12 += 1
    elif step > 5:
        r = (step + 1) % 7
        if r == 0:
            d6 += 2
        elif r == 1:
            d8 += 1
            d6 += 1
        elif r == 2:
            d8 += 2
        elif r == 3:
            d10 += 1
            d8 += 1
        elif r == 4:
            d10 += 2
        elif r == 5:
            d12 += 1
            d10 += 1
        elif r == 6:
            d12 += 2
        if step > 12:
            d12 += (step - 6) // 7

    return (d12, d10, d8, d6, d4)

################################################################################

def printStep(step):

    '''
    converts the submitted step tuple into a string

    arguments
        step: tuple of 5 non-negative integers (number of each die in the step)

    returns
        stepString: string describing the step
    '''

    dieNotation = ("d12", "d10", "d8", "d6", "d4")
    stepString = ""
    
    for die in range(5):
        numDice = step[die]
        if numDice == 1:
            stepString += dieNotation[die] + "+"
        elif numDice > 1:
            stepString += str(numDice) + dieNotation[die] + "+"

    if stepString == "":
        return "Step 0"
    else:
        return stepString[0:-1]

################################################################################

def rollStep(step):

    '''
    rolls the dice in the submitted step tuple

    arguments
        step: tuple of 5 non-negative integers (number of each die in the step)

    output (only if PRINT_DEBUG is True)
        the die being rolled
        the total rolled on that die
        the string description of the step
        the total roll for that step

    returns
        total: integer (the total of the step roll)
    '''

    total = 0
    die = 12

    stepDice = diceStep(step)

    for numDice in stepDice:
        if numDice > 0:
            for roll in range(numDice):
                if PRINT_DEBUG:
                    print("  d" + str(die) + ": ", end = "")
                dieResult = rollDie(die)
                if PRINT_DEBUG:
                    print(" = " + str(dieResult))
                total += dieResult
        die -= 2

    return total

################################################################################

def rollDie(die):

    '''
    rolls an individual exploding die

    arguments (only if PRINT_DEBUG is True)
        die: non-negative integer (max value of the die to be rolled)
        
    output
        the number rolled on that die, including any explosions
        
    returns
        total: integer (the total roll for that die, including explosions)
    '''

    total = 0

    roll = random.randint(1, die)
    total += roll

    if PRINT_DEBUG:
        print(str(roll), end = "")
    
    if total == die:
        if PRINT_DEBUG:
            print(" + ", end = "")
        total += rollDie(die)

    return total

################################################################################

def isInt(s):

    '''
    checks to see if a string represents an integer

    arguments
        s: string

    returns
        True or False
    '''
    
    try: 
        int(s)
        return True
    except ValueError:
        return False

################################################################################

def main():

    '''
    the main function

    output
        the string representations for steps 0 to 30
        the string representation of the input step
        the total of the roll for the input step

    input
        stepToRoll: string (q to quit or a step to roll)
    '''

    for n in range(31):
        print("Step", n, "=", printStep(diceStep(n)))

    print()
    
    while True:
        print()
        stepToRoll = input("Enter a step to roll (Q to quit): ")
        if stepToRoll.upper() == "Q":
            break
        elif isInt(stepToRoll):
            stepToRoll = int(stepToRoll)
        else:
            print("\n\n\n!!! ERROR: input must be an integer or Q !!!\n\n\n")
            break
        print("Rolling " + printStep(diceStep(stepToRoll)) + ":",
              rollStep(stepToRoll))

    print("\n\nGoodbye!")

################################################################################

main()
