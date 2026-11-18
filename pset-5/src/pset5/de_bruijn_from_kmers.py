def deBruijnFromKmers(patterns: list[str]) -> list[list[str]]:
    """Return the de Bruijn graph of the k-mers as rows [source, destination] (BA3E).

    Each row contains one directed edge, with the source first.
    Row order does not matter. Preserve duplicate rows for parallel edges.
    """
    prefixes = set()
    suffixes = set()
    edgeGraph = []

    for x in patterns:
        prefixes.add(x[:-1])
        suffixes.add(x[1:])
    

    for x in prefixes:
        matches = []
        for y in suffixes:
            if(x[1:]==y[:-1]):
                matches.append(y)
        edgeGraph.append([x,matches]) #is it ok to return it as a list if there are two destinations for one source?

    
    return edgeGraph


meow = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
print(deBruijnFromKmers(meow))

