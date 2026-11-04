def hammingDistance(p: str, q: str) -> int:
    # TODO: Write your code here.
    count = 0
    i=0
    while i< len(p):
        if p[i:i+1] != q[i:i+1]:
            count += 1
        i += 1

    return count

def approximatePatternMatching(pattern: str, text: str, d: int) -> list[int]:
    matches = []

    i = 0
    while i < len(text)-len(pattern):
        if(hammingDistance(pattern, text[i:i+(len(pattern))])<=d):
            matches.append(i)
        i = i+1

    return matches

