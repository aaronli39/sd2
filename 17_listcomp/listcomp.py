# Xiaojie(Aaron) Li, Hasif Ahmed
# Softdev2 pd8
# K17 -- PPFTLCW
# 2019-04-14

def first(l):
    counter = 0
    ret = []
    for i in range(l):
        ret.append(str(counter) + str(counter))
        counter += 2
    return ret

def firstLis(l):
    ret = [str(i * 2) + str(i * 2) for i in range(l)]
    return ret

def second(l):
    counter = 7
    ret = []
    for i in range(l):
        ret.append(counter)
        counter += 10
    return ret

def secondLis(l):
    ret = [7 + (10 * i) for i in range(l)]
    return ret

def third(l):
    ret = [0, 0, 0]
    for i in range(l):
        ind = len(ret)
        ret.append(ret[ind - 3])
        ret.append(ret[ind - 2] + 1)
        ret.append(ret[ind - 1] + 2)
    return ret

def thirdLis(l):
    ret = []

def fourth():
    ret = []
    nums = [2,3,4,5,6,7,8,9]
    notprime = [0,2,3,5,7]
    for i in range(100):
        for x in nums:
            if i in notprime:
                break 
            if i % x == 0:
                ret.append(i)
                break
    return ret

def fourthLis():
    ret = [i for i in range(100) for x in [2, 3, 4, 5, 6, 7, 8, 9] if i % x == 0 and i not in [0, 2, 3, 5, 7]]
    return list(set(ret)) 

def fifth():
    ret, state = [], True
    for i in range(2, 101):
        state = True
        for x in range(2, i):
            if i % x == 0:
                state = False
                break 
        if state: ret.append(i)
    return ret

def fifthLis():
    ret = [i for i in range(2, 101) if True not in [True if i % x == 0 else False for x in range(2, i)]]
    return ret

def sixth(l):
    ret = [1]
    for i in range (2, l + 1):
        if l % i == 0: ret.append(i)
    return ret

def sixthLis(l):
    ret = [i for i in range(1, l + 1) if l % i == 0]
    return ret

def seventh(l):
    ret = []
    for i in range(len(l[0])):
        temp = []
        for x in range(len(l)):
            temp.append(l[x][i])
        ret.append(temp)
    return ret

def seventhLis(l):
    ret = [[l[x][i] for x in range(len(l))] for i in range(len(l[0]))]
    return ret
    
print(first(5))
print(firstLis(5))
print(second(5))
print(secondLis(5))
print(third(5))
print(fourth())
print(fourthLis())
print(fifth())
print(fifthLis())
print(sixth(66))
print(sixthLis(66))
print(seventh([[1, 2, 3], [5, 9, 1]]))
print(seventhLis([[1, 2, 3], [5, 9, 1]]))
