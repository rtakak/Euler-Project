
def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def solve(n):
    string = ""
    list = [digit for digit in range(10)]
    for digit in range(10,0, -1):
        print(digit)
        diff = factorial(digit-1)
        for step in range(1,len(list)+1):
            if diff * step >= n:
                string += str(list[step-1])
                del list[step-1]
                n = n - diff * (step-1)
                break
    print(string)
    return string


solve(1000000)