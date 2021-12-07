import time
def solve():
    last_two = [1,1]
    sum = 0
    while last_two[1] <= 4000000:
        last_two[0], last_two[1] = last_two[1], last_two[0] + last_two[1]
        if not last_two[1] % 2:
            sum += last_two[1]
    print(sum)

start = time.time()
for x in range(100):
    solve()
print(time.time()-start)