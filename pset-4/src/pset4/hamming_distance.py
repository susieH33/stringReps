def hammingDistance(p: str, q: str) -> int:
    # TODO: Write your code here.
    count = 0
    i=0
    while i< len(p):
        if p[i:i+1] != q[i:i+1]:
            count += 1
        i += 1

    return count
