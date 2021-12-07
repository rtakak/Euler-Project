def solve():
    number = 2**1000
    sum = 0
    print(number)
    while number > 0:
        sum += number % 10
        number //= 10
    print(sum)

def solve2():
    print(sum(int(x) for x in str(2**1000)))

solve2()