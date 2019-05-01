# def inc(x):
#     return x + 1

# f = inc
# print(f)
# print(f(10))

def outer(x):
    def contains(l):
        return x in l
    return contains

contains_15 = outer(15)
print(contains_15([1, 2, 3, 4, 5]))
print(contains_15([13, 14, 15, 16, 17]))
print(contains_15(range(1, 20)))

# del outer
# outer(42)

# contains_15(range(14, 20))

def r1(x):
    def ret(l):
        return x * l
    return ret

hallo = r1(2)
print(hallo("hello"))

def out():
    x = "foo"
    def inner():
        x = "bar"
    inner()
    return x

print(out())

def make_counter():
    x = 0
    def inc(x):
        nonlocal x
        x = x + 1
    inc()
    print(x)

temp = make_counter()