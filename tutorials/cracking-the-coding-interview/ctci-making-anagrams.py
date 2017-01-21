def number_needed(a, b):
    letterNumbers = [getLetterNumbers(a), getLetterNumbers(b)]
    return getNumberOfDeletedLetters(letterNumbers, 0) 
    
def getLetterNumbers(str):
    letterDict = {}

    for c in str:
        if c in letterDict:
            letterDict[c] += 1
        else:
            letterDict[c] = 1

    return letterDict 

def getNumberOfDeletedLetters(letterNumbers, numberOfDeletedLetters):
    a = letterNumbers[0]
    b = letterNumbers[1]

    for c in a:
        if c in a and c in b:
            numberOfDeletedLetters += abs(a[c] - b[c])
            n = a[c] if a[c] < b[c] else b[c]
            a[c] = b[c] = n
        elif bool(c in a) != bool(c in b):
            if c in a:
                numberOfDeletedLetters += a[c]
                a[c] = 0
            elif c in b:
                numberOfDeletedLetters += b[c]
                b[c] = 0

    for c in b:
        if c in a and c in b:
            numberOfDeletedLetters += abs(a[c] - b[c])
            n = a[c] if a[c] < b[c] else b[c]
            a[c] = b[c] = n
        elif bool(c in a) != bool(c in b):
            if c in a:
                numberOfDeletedLetters += a[c]
                a[c] = 0
            elif c in b:
                numberOfDeletedLetters += b[c]
                b[c] = 0

    return numberOfDeletedLetters

a = "tttttttttttttttttttttttttttttttttttttsssssssssssssssss"
b = "sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"

# a = raw_input().strip()
# b = raw_input().strip()

print number_needed(a, b)