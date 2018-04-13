"""Whiteboard projects

   Potential whiteboard project questions

       created
           by:  R. G. Blaine
           on:  April, 9, 2018
"""

# imports
import random


################################################################################

def listFibs(n):

    '''Creates and prints a list of the first n fibonacci numbers.

    arguments:
        n : integer 2 or greater

    returns:
        none
    '''

    # variables
    fibNums = []            # list to hold the fibonacci numbers
    fibNums.append(0)       # the 1st fibonacci number
    fibNums.append(1)       # the 2nd fibonacci number

    # error handling
    if (n < 2) or (n != int(n)):
        print("\n\n\n !!! Argument must be an integer 2 or greater !!! \n\n\n")
        return

    # adds the next (n - 2) fibonacci numbers to the list
    for i in range(n - 2):
        fibNums.append(fibNums[i] + fibNums[i + 1])

    # formats and prints the list
    printIntList(fibNums)

    # spacer
    print()

    return

################################################################################

def listPrimes(n):

    '''Creates and prints a list of the first n prime numbers.

    arguments:
        n : integer 1 or greater

    returns:
        none
    '''

    # variables
    primeNums = []          # list to hold the prime numbers
    primeNums.append(2)     # the 1st prime number
    num = 3                 # the 2nd prime number

    # error handling
    if (n < 1) or (n != int(n)):
        print("\n\n\n !!! Argument must be an integer 1 or greater !!! \n\n\n")
        return

    # add prime numbers to the list until it of length n
    while len(primeNums) < n:
        isPrime = True      # flag to see if the number is prime

        # loop through all possible divisors up to num/2
        for i in range(2, num // 2 + 1):
            
            # if the number divides evenly flag it as not prime
            if (num/i) == int(num/i):
                isPrime = False
                
        # if the number is prime, append it to the list
        if isPrime:
            primeNums.append(num)

        # increment the number to check
        num += 1

    # format and print the list
    printIntList(primeNums)

    # spacer
    print()

    return
    
################################################################################

def makeDeck():

    '''Create and return an unsorted deck of cards and return it as a list.

    arguments:
        none

    returns:
        unsorted list of cards (strings)
    '''
    
    # variables
    columnWidth = 20        # width of the columns
    numColumns = 4          # number of columns
    
    deck = []               # list to hold the deck

    # creat deck
    for suit in ('Clubs', 'Diamonds', 'Hearts', 'Spades'):
        for faceValue in ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'):
            deck.append(faceValue + ' of ' + suit)

    # print deck
    printDeck(deck)
            
    # spacer
    print()

    # return deck
    return deck

################################################################################

def shuffleDeck(deck):

    '''Shuffle and print a deck of cards.

    arguments:
        deck : an unsorted list of cards (strings)

    returns:
        none
    '''

    # variables
    columnWidth = 19        # width of the coloumns
    numColumns = 4          # number of columns
    
    shuffledDeck = []       # list to hold the deck

    # shuffle deck
    for i in range(52):
       shuffledDeck.append(deck.pop(random.randint(0, 51 - i)))

    # print deck
    printDeck(shuffledDeck)

    # spacer
    print()

    return

################################################################################

def printDeck(deck):

    '''Prints the submitted list representing a deck cards

    arguments:
        deck : a list of strings representing a deck of 52 cards

    returns:
        none
    '''

    # error handling
    if len(deck) != 52:
        print("\n\n\n !!! Illegal deck!  Must be 52 elements !!!\n\n\n")
        return

    # print the deck
    for faceIndex in range(13):
        for suitIndex in range(4):
            cardIndex = faceIndex + suitIndex * 13
            print(" " * (19 - len(deck[cardIndex])), end = "")
            print(deck[cardIndex], end = "")
        print()

    return

################################################################################

def bubbleSort(listSize):

    '''Creates a list of random integers then sorts, reverses, and re-sorts it.

    arguments:
        listSize: integer (2 or greater)

    returns:
        none
    '''

    # define variables
    numList = []        # the list

    # error handling
    if (listSize < 2) or (listSize != int(listSize)):
        print("\n\n\n !!! Argument must be integer of value 2+ !!!\n\n\n")

    # create the random list
    for n in range(listSize):
        numList.append(random.randint(100, 999))

    print("Random list:", numList)

    # bubble sort
    n = len(numList) - 1            # maximum number of passes
    for p in range(n):              # pass counter
        exchange = False            # exchange flag
        for i in range(n - p):      # list index
            # exchange elements if the 1st one is larger
            if numList[i] > numList[i + 1]:
                numList[i], numList[i + 1] = numList[i + 1], numList[i]
                exchange = True     # flag that an exchange was made
        print("    Pass #" + str(p + 1) + ":", numList)
        # end sort if no exchanges were made
        if not exchange:
            break

    # built-in Python sort
    numList.sort(reverse = True)
    print("   Reversed:", numList)
    numList.sort()
    print("  Re-sorted:", numList)
    print("2nd largest:", numList[-2])

    return

################################################################################

def printIntList(intList):

    '''Formats and prints a list of integers.

    arguments:
        intList : a list of integers
    '''

    # variables
    columnWidth = len(("{:,}".format(intList[-1]))) + 2     # column width
    screenWidth = 80                                        # screen width
    numColumns = screenWidth // columnWidth                 # number of columns

    # ensure that the number of columns is at least 1
    if numColumns < 1:
        numColumns = 1

    # print list
    count = 1       # counter to track when to end a line

    # go through the list
    for n in intList:

        # error checking
        if n != int(n):
            print("\n\n\n !!! List must contain only integers !!! \n\n\n")
            return

        # print column
        x = ("{:,}".format(n))
        print(" " * (columnWidth - len(x)), end = "")
        print(x, end = "")
        
        # go to next line once the appropriate number of columns have printed
        if (count % numColumns) == 0:
            print()

        # increment the count
        count += 1

    return

################################################################################

# run the functions

print("Fibonacci numbers:")
listFibs(50)

print("\nPrime numbers:")
listPrimes(330)

print("\n\nNew deck:")
newDeck = makeDeck()

print("\nShuffled deck:")
shuffleDeck(newDeck)

print("\nBubble sort:")
bubbleSort(10)
