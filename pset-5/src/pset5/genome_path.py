def stringSpelledByGenomePath(patterns: list[str]) -> str:
   i=0
   k = len(patterns[0])
   genome = ""
   while i<k:
      substring = patterns[i]
      genome = genome + substring[0:1]
      i = i+1
    
   genome = genome + patterns[-1]

   return genome

meow = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
print(stringSpelledByGenomePath(meow))