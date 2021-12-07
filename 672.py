import time
def g_function(value, counter=0):
    if value == 1:
        return counter
    elif value % 7:
        value += 1
        counter += 1
    else:
        value /= 7
    return g_function(value, counter)

def s_func(n):
    return sum(g_function(value) for value in range(1, n+1))
print("bas")
start = time.time()
num = (7**10 - 1) // 11
print(s_func(num))
print("time: ", time.time() - start)