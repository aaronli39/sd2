# Xiaojie(Aaron) Li, Hasif Ahmed
# Softdev2 pd8
# 2019-04-15
# K18 -- ListComp

# pythagorean triples
def triples(n):
    return [(a, b, c) for a in range(2, n + 1) for b in range(a, n + 1) for c in range(b, n + 1) if (a * a) + (b * b) == c * c]

# quiccccsort
def qsort(inp):
    if inp == []: return []
    return qsort([i for i in inp[1:] if i <= inp[0]]) + [inp[0]] + qsort([i for i in inp[1:] if i > inp[0]])
    
print(triples(17))
print(qsort([1, 5, 7, 1, 3, 9, 10, 6, 8, 5, 3]))