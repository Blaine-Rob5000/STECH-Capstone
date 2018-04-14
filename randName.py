import random

def randName():

    first = ["All", "Bob", "Can", "Dig", "Ema", "Fra", "Gro", "Hil", "Ike",
             "Jer", "Kal", "Lee", "Mom", "Nan", "Old", "Pat", "Qua", "Rob",
             "Sam", "Tim", "Uma", "Val", "Wub", "Xim", "Yar", "Zoe"]

    middle = ["al", "be", "co", "di", "eh", "fa", "go", "hu", "ig", "jo",
              "ky", "la", "me", "nu", "op", "pi", "qu", "re", "so", "ta",
              "um", "va", "we", "xi", "ym", "za"]

    last  = ["ark", "Bob", "cer", "Dug", "elk", "fig", "gan", "hop", "ine",
             "Joe", "kin", "Loo", "met", "net", "oom", "per", "qat", "rem",
             "set", "top", "ult", "ver", "wet", "xer", "yay", "zit"]

    name = ""
    name += first[random.randint(0, len(first) - 1)]
    if random.randint(1, 100) > 50:
        name += middle[random.randint(0, len(middle) -1)]
    name += last[random.randint(0, len(last) - 1)]

    return name

def main(numNames = 100):
    maxLength = 8
    numColumns = 5 # 80 // (maxLength + 3)
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

main()
