"""Rosalind BA1E: Find Patterns Forming Clumps in a String."""
def patternCount(text: str, pattern: str) -> int:
    count = 0
    a = 0
    while a < (len(text)-len(pattern))+1:
        if(text[a:a+len(pattern)]) == pattern:
            count = count+1
        a = a+1
    return count


def findClumps(genome: str, k: int, L: int, t: int) -> set[str]:
    qualPatterns = set()
    x = 0

    while x <= len(genome) - L:
        frame = genome[x:x + L]
        y = 0

        while y <= len(frame) - k:
            pattern = frame[y:y + k]

            if patternCount(frame, pattern) >= t:
                qualPatterns.add(pattern)

            y += 1

        x += 1

    return qualPatterns
