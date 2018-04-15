
"""
Random name generator
    by R. G. Blaine
    on 4/14/2018
"""


import random

############################################################

def nameInit():
    global ACCENT, VOWELS, CONSONANTS, SYLLABLES
    ACCENT = [" ", "'", "-"]
    VOWELS = ["a", "e", "i", "o", "u", "y"]
    CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    SYLLABLES = []

    for letter1 in VOWELS:
        for letter2 in VOWELS:
            if not ("yy" in (letter1 + letter2)):
                SYLLABLES.append(letter1.upper() + letter2)

    for letter1 in VOWELS:
        for letter2 in CONSONANTS:
            if not ("yy" in (letter1 + letter2)):
                SYLLABLES.append(letter1.upper() + letter2)

    for letter1 in CONSONANTS:
        for letter2 in VOWELS:
            if not ("yy" in (letter1 + letter2)):
                SYLLABLES.append(letter1.upper() + letter2)

    for letter1 in VOWELS:
        for letter2 in VOWELS:
            for letter3 in CONSONANTS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

    for letter1 in VOWELS:
        for letter2 in CONSONANTS:
            for letter3 in VOWELS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

    for letter1 in VOWELS:
        for letter2 in CONSONANTS:
            for letter3 in CONSONANTS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

    for letter1 in CONSONANTS:
        for letter2 in VOWELS:
            for letter3 in VOWELS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

    for letter1 in CONSONANTS:
        for letter2 in VOWELS:
            for letter3 in CONSONANTS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

    for letter1 in CONSONANTS:
        for letter2 in CONSONANTS:
            for letter3 in VOWELS:
                if not ("yy" in (letter1 + letter2 + letter3)):
                    SYLLABLES.append(letter1.upper() + letter2 + letter3)

############################################################

def randName():

    '''
    The name generator.

    returns:  string (representing the random name)
    '''

    name = SYLLABLES[random.randint(0, len(SYLLABLES) - 1)]
    
    if random.randint(1, 100) <= 10:
        name += ACCENT[random.randint(0, len(ACCENT) -1)]
        
    if random.randint(1, 100) <= 50:
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]

        checkThis = (name[-2:] + syllable[:2])
        while threeSame(checkThis):
            syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
            checkThis = (name[-2:] + syllable[:2])
            
        if (name[-1] not in ACCENT) and (random.randint(1, 100) <= 90):
            syllable = syllable.lower()

        name += syllable
        
        if random.randint(1, 100) <= 10:
            name += ACCENT[random.randint(0, len(ACCENT) -1)]
            
    syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
    
    checkThis = (name[-2:] + syllable[:2])
    while threeSame(checkThis):
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
        checkThis = (name[-2:] + syllable[:2])
        
    if (name[-1] not in ACCENT) and (random.randint(1, 100) <= 90):
        syllable = syllable.lower()

    name += syllable

    return name

############################################################

def threeSame(stringToCheck):
    '''
    checks for all vowels or all consonants
    '''
    if threeConsonants(stringToCheck) or threeVowels(stringToCheck):
        return True
    return False

############################################################

def threeConsonants(stringToCheck):
    '''
    checks the string to see if it contains 3 consecutive consonants
    '''
    stringToCheck = stringToCheck.lower()
    counter = 0
    flag = False
    for letter in stringToCheck:
        if (letter in CONSONANTS) and (letter != 'y'):
            counter += 1
            if counter > 2:
                flag = True
        else:
            counter = 0
    return flag

############################################################

def threeVowels(stringToCheck):
    '''
    checks the string to see if it contains 3 consecutive vowels
    '''
    stringToCheck = stringToCheck.lower()
    counter = 0
    flag = False
    for letter in stringToCheck:
        if (letter in VOWELS) and (letter != 'y'):
            counter += 1
            if counter > 2:
                flag = True
        else:
            counter = 0
    return flag

############################################################

def main(numNames = 40):
    maxLength = 10
    numColumns = 4 # 80 // (maxLength + 3)
    name = []

    while len(name) < numNames:
        name.append(randName())

    name.sort()

    i = 0
    while i < len(name):
        print(name[i], end = "")
        if i < len(name) - 1:
            print(",", end = "")
        if (i + 1) % numColumns != 0:
            print(" " * (maxLength - len(name[i]) + 2), end = "")
        else:
            print()
        i += 1


############################################################

nameInit()

print("Number of Syllables:", len(SYLLABLES))
num = len(SYLLABLES)**3 * len(ACCENT)**2
print("Approx number of possible names: {:,}\n".format(num))

main(120)

