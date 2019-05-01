# Xiaojie(Aaron) Li
# Softdev2 pd8
# K22 -- Closure
# 2019-04-30

def repeat(x):
    def inner(l):
        return x * l
    return inner

def make_counter():
    x = 0
    def inc():
        nonlocal x
        x += 1
        return x
    return inc

r1, r2 = repeat("hello"), repeat("goodbye")
print(r1, r2, repeat("cool")(3))

ctr1 = make_counter()
print(ctr1)
print(ctr1)
ctr2 = make_counter()
print(ctr2)
print(ctr2)
print(ctr1)