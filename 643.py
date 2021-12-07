from math import gcd
from functools import cache

@cache
def isPowerOfTwo(x):
    return (x and (not (x & (x - 1))))

def solve(n):
    counter = 0
    for p in range(2, n, 2):
        for q in range(p + 2, n + 1, 2):
            if isPowerOfTwo(gcd(p, q)):
                counter += 1
    print(counter)

solve(10**6
      )