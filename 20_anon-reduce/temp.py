'''
Pineappols -- Xiaojie(Aaron) Li, Hasif Ahmed
SoftDev2 pd8
K20 -- Reductio ad Absurdum
2019-04-17
'''

import re, functools

with open("text.txt", "rU") as txt:
    inp = txt.read()

# this searches for most frequent word or phrase
def freqWords(words):
    return len([i for i in range(0, len(inp) - len(words)) if inp[i: i + len(words)] == words])

word = re.findall(r'\w+', inp)
words = list(set(word))

# this returns most frequent word in moby dick
def mostFreq():
    return functools.reduce(lambda a, b: a if a[1] > b[1] else b, [(i, word.count(i)) for i in words])

print(freqWords("the"))
print(mostFreq())