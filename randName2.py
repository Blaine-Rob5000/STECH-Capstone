
"""
Random name generator
    by R. G. Blaine
    on 4/14/2018
"""


import random

def nameInit():
    global ACCENT, VOWELS, CONSONANTS, SYLLABLES
    ACCENT = [" ", "'", "-"]
    VOWELS = ["a", "e", "i", "o", "u", "y"]
    CONSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
                  "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    SYLLABLES = []

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            SYLLABLES.append(let1.upper() + let2)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            SYLLABLES.append(let1.upper() + let2)

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            for let3 in VOWELS:
                SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in VOWELS:
        for let2 in CONSONANTS:
            for let3 in CONSONANTS:
                SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            for let3 in VOWELS:
                SYLLABLES.append(let1.upper() + let2 + let3)

    for let1 in CONSONANTS:
        for let2 in VOWELS:
            for let3 in CONSONANTS:
                SYLLABLES.append(let1.upper() + let2 + let3)


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
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
        while (name[-1] in CONSONANTS) and (name[-2] in CONSONANTS) and (syllable[0] in CONSONANTS):
            syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
        while (name[-1] in VOWELS) and (name[-2] in VOWELS) and (syllable[0] in VOWELS):
            syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
        name += syllable
        if random.randint(1, 100) < 11:
            name += ACCENT[random.randint(0, len(ACCENT) -1)]
    syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
    while (name[-1] in CONSONANTS) and (name[-2] in CONSONANTS) and (syllable[0] in CONSONANTS):
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
    while (name[-1] in VOWELS) and (name[-2] in VOWELS) and (syllable[0] in VOWELS):
        syllable = SYLLABLES[random.randint(0, len(SYLLABLES) -1)].lower()
    name += syllable

    return name

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

nameInit()
main(200)

print("\n\nSYLLABLES:",len(SYLLABLES))
print("\nSYLLABLES:",len(SYLLABLES)**3 * len(ACCENT)**2)
