def deBruijnFromString(k: int, text: str) -> list[list[str]]:
    """Return the de Bruijn graph of text as rows [source, destination] (BA3D).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    #need to ask about why the edges are k-1?
    i = 0
    prefixes = set()
    suffixes = set()
    kmer = []
    edgeGraph = []

    while i<len(text)-k+1:
        kmer = text[i:i+k]
        prefixes.add(kmer[:-1])  #not actually the prefixes and suffixes but im confused
        suffixes.add(kmer[1:])
        #print(prefixes)
        i = i+1
    
    print(prefixes)
    print(suffixes)
    for x in prefixes:
        print(x)
        for y in suffixes:
            if(x[1:]==y[:-1]):
                edgeGraph.append([x,y]) 

    return edgeGraph


#is it ok to return duplicates as their own pair or should i combine them so its x -> y, y
print(deBruijnFromString(4, "AAGATTCTCTAC")) 
