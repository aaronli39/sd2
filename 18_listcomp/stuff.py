# Xiaojie(Aaron) Li, Hasif Ahmed
# Softdev2 pd8
# K18 -- PPFTLCW
# 2019-04-15

# pythagorean triples
def triples(n):
    return [(a, b, c) for a in range(2, n + 1) for b in range(a, n + 1) for c in range(b, n + 1) if (a * a) + (b * b) == c * c]

# quiccccsort
def qsort(inp):
    

print(triples(17))