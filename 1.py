import time


def solve():
    sum = 0
    for number in range(100):
        if not number % 3 or not number % 5:
            sum += number
    print(sum)


def solve2():
    x3 = 999 // 3
    sumof3s = 3 * x3 * (x3 + 1) / 2
    x5 = 999 // 5
    sumof5s = 5 * x5 * (x5 + 1) / 2
    x15 = 999 // 15
    sumof15s = 15 * x15 * (x15 + 1) / 2
    sum = sumof5s + sumof3s - sumof15s
    print(sum)


solve2()
time.sleep(2)
times = 1000000
start1 = time.time()
for count in range(times):
    solve()
result1 = time.time() - start1
print("r1 done")

start2 = time.time()
for count in range(times):
    solve2()
result2 = time.time() - start2
print("r2 done")

print(result1)
print(result2)
print(result1 * 100 / result2)
