import itertools

def reverseComplement(text: str) -> str:
    revComp = ""

    for x in reversed(text):
        if x == "A":
            revComp = revComp + "T"
        elif x == "T":
            revComp = revComp + "A"
        elif x == "C":
            revComp = revComp + "G"
        elif x == "G":
            revComp = revComp + "C"
    
    return revComp

def hammingDistance(p: str, q: str) -> int:
    # TODO: Write your code here.
    count = 0
    i=0
    while i< len(p):
        if p[i:i+1] != q[i:i+1]:
            count += 1
        i += 1

    return count

def frequentWordsWithMismatches(text: str, k: int, d: int) -> set[str]:
    #1 generate all possible combinations of kmers big inefficient
    chars = 'ACGT'
    
    p = itertools.product(chars, repeat=k)

    possiblePatterns = [''.join(x) for x in p]

    possiblePatterns.sort()

    matches = [0]*(4**k)

    #2 check every single substring lol
    i = 0 #index for going thru text

    while i < len(text)-k:
        kmer = text[i:i+k]
        x = 0 #index for checking each substring with possiblePatterns
        while x<len(possiblePatterns):
            if (hammingDistance(possiblePatterns[x],kmer)<=d):
                #print(x)
                matches[x]= matches[x]+1
            x = x+1
        i = i+1
   
    #print(matches)
    maxCount = max(matches)
    #print(maxCount)
    allMax = []

    y = 0
    while y < len(matches):
        if(matches[y]==maxCount):
            #print(y)
            allMax.append(possiblePatterns[y])
        y = y+1

    return allMax

def frequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int) -> set[str]:
    #1 generate all possible combinations of kmers big inefficient
    chars = 'ACGT'
    
    p = itertools.product(chars, repeat=k)

    possiblePatterns = [''.join(x) for x in p]

    possiblePatterns.sort()

    matches = [0]*(4**k)
    #revCompMatches = [0]*(4**k)

    #2 check every single substring lol
    i = 0 #index for going thru text

    while i < len(text)-k:
        kmer = text[i:i+k]
        revCompkmer = reverseComplement(text[i:i+k])
        x = 0 #index for checking each substring with possiblePatterns
        while x<len(possiblePatterns):
            if (hammingDistance(possiblePatterns[x],kmer)<=d):
                #print(x)
                matches[x]= matches[x]+1
            if (hammingDistance(possiblePatterns[x],revCompkmer)<=d):
                matches[x]= matches[x]+1
            x = x+1
        i = i+1
   
    #print(matches)
    maxCount = max(matches)
    #print(maxCount)
    allMax = []

    y = 0
    while y < len(matches):
        if(matches[y]==maxCount):
            #print(y)
            allMax.append(possiblePatterns[y])
        y = y+1

    #finalSet = set(normalMax + allMax)
    #print(allMax)

    return allMax

print(frequentWordsWithMismatchesAndReverseComplements("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
    




