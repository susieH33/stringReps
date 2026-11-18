def stringComposition(k: int, text: str) -> list[str]:
    i = 0

    composition = []
    while i < len(text)-k+1:
        substring = text[i:i+k]
        composition.append(substring)
        i = i+1
    composition.sort()
    return composition
   

print(stringComposition(5, "CAATCCAAC"))
