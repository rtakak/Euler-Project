def solve():
    summ = 0
    list = []
    digit = 2
    max = digit * (9 ** 5)
    while len(str(max)) != digit:
        digit += 1
        max = digit * (9 ** 5)

    for number in range(10,max):
        digits = str(number)
        if sum(int(digit) ** 5 for digit in digits) == number:
            list.append(number)
            summ += number

    print(list)
    print(summ)

solve()