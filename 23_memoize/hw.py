# Xiaojie(Aaron) Li
# Softdev2 pd8
# K23 -- Memoize with closure
# 2019-05-02

def memoize(f):
    memo = {}
    def inner(x):
        if x in memo: memo[x] = f(x)
        return memo[x]
    return inner

@memoize
def fib(x):
    if x == 0: return 0
    if x == 1: return 1
    return fib(x - 1) + fib(x - 2)

fibbo = memoize(fib)
print(fibbo(5))