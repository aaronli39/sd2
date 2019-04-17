with open("text.txt", "rU") as txt:
    inp = txt.read().split("\n")
    inp = [i.split(" ") for i in inp]
    
inp = inp[:len(inp) - 8]
print(inp)

def freq(word):
    return len([x for i in inp for x in i if x == word])

def freqWords(words):
    return 

print(freq("the"))