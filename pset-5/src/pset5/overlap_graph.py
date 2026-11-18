def overlapGraph(patterns: list[str]) -> list[list[str]]:
    edgeGraph = []

    i = 0

    while i<len(patterns):
        fr = patterns[i]
        frSuf = fr[1:]
        for x in patterns:
            toPre = x[:-1]
            if frSuf == toPre:
                edgeGraph.append([fr,x])
        i = i+1
    
    return edgeGraph

print(overlapGraph(["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]))

# this doesnt account for if theres two matches ?? try more test cases later