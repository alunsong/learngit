import time


def f(n):
    #time.clock()
    if n == 1:
        return 1
    if n ==2:
        return 2
    if n > 2:
        return f(n - 1) + f(n - 2)

s1 = f(100)
print("s1=",s1)


def f(n):
    res = [0 for i in range(n+1)]
    res[1] = 1
    res[2] = 2
    for i in range(3, n+1):
        res[i] = res[i - 1] + res[i -2]
    return res[n]

s2 = f(100)
print("s2=",s2)


cache = {}
def fib(n):
    if n not in cache.keys():
        cache[n] = _fib(n)
    return cache[n]

def _fib(n):
    if n == 1 or n == 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
s3 = fib(100)
print("s3=",s3)
