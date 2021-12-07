def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def comb(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))

def solve():
    list = []
    counter = 0
    for n in range(1,101):
        for r in range(n+1):
            if comb(n, r) >= 10**6:
                counter += 1
                #list.append(comb(n,r))
    print(counter)

solve()