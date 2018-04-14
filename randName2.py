
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

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            if not ("yy" in (let1 + let2)):
                SYLLABLES.append(let1.upper() + let2)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            if not ("yy" in (let1 + let2)):
                SYLLABLES.append(let1.upper() + let2)

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            for let3 in VOWELS:
                if not ("yy" in (let1 + let2 + let3)):
                    SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            for let3 in CONSONANTS:
                if not ("yy" in (let1 + let2 + let3)):
                    SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            for let3 in VOWELS:
                if not ("yy" in (let1 + let2 + let3)):
                    SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            for let3 in CONSONANTS:
                if not ("yy" in (let1 + let2 + let3)):
                    SYLLABLES.append(let1.upper() + let2 + let3)

############################################################

def randName():

    '''
    The name generator.

    returns:  string (representing the random name)
    '''

    name = ""
    
    name += SYLLABLES[random.randint(0, len(SYLLABLES) - 1)]
    
    if random.randint(1, 100) < 11:
        name += ACCENT[random.randint(0, len(ACCENT) -1)]
        
    if random.randint(1, 100) < 51:
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]

        last3 = name[-2:] + syllable[0].lower()
        
        while allConsonants(last3) or allVowels(last3):
            syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
            last3 = name[-2:] + syllable[0].lower()
            
        if (name[-1] not in ACCENT) and (random.randint(1, 100) <= 90):
            syllable = syllable.lower()

        name += syllable
        
        if random.randint(1, 100) < 11:
            name += ACCENT[random.randint(0, len(ACCENT) -1)]
            
    syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
    

    last3 = name[-2:] + syllable[0].lower()
        
    while allConsonants(last3) or allVowels(last3):
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)]
        last3 = name[-2:] + syllable[0].lower()

    if (name[-1] not in ACCENT) and (random.randint(1, 100) <= 90):
        syllable = syllable.lower()

    name += syllable

    return name

############################################################

def allConsonants(stringToCheck):
	'''
	checks the string to see if it is all consonants
	'''
	for letter in stringToCheck:
		if letter not in CONSONANTS: return False
	return True

############################################################

def allVowels(stringToCheck):
	'''
	checks the string to see if is all vowels
	'''
	for letter in stringToCheck:
		if letter not in VOWELS: return False
	return True

############################################################

def main(numNames = 100):
    maxLength = 10
    numColumns = 4 # 80 // (maxLength + 3)
    name = []

    while len(name) < numNames:
        name.append(randName())

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


main(200)

