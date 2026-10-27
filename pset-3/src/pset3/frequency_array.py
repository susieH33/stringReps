"""Rosalind BA1K: Generate the Frequency Array of a String."""
import itertools 

def frequencyArray(text: str, k: int) -> list[int]:
    """Return counts for all 4**k DNA k-mers in lexicographic order.

    Use alphabet order A, C, G, T. Include zero counts and count
    overlapping occurrences. Assume uppercase DNA and 1 <= k <= len(text).
    """
    chars = 'ACGT'
    
    p = itertools.product(chars, repeat=k)

    patterns = [''.join(x) for x in p]

    patterns.sort()
    
    freqArr = [0]*(4**k)
    
    i = 0
    while i <= len(text)-k:
        substr = text[i:i+k]
        index = patterns.index(substr)
        freqArr[index] += 1
        i = i+1

    return freqArr