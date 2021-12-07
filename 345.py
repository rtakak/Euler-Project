import numpy as np

array1 = [[7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
          [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
          [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
          [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
          [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
          [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
          [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
          [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
          [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
          [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
          [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
          [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
          [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
          [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
          [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805]]

array2 = [[7, 53, 183, 439, 863], [497, 383, 563, 79, 973], [287, 63, 343, 169, 583], [627, 343, 773, 959, 943], [767, 473, 103, 699, 303]]


def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


def perm(n, r):
    return factorial(n) // factorial(n - r)


class contain:
    best = 0
    counter = 0
    best_sum = 0


c = contain()
divider = 0
tops = []

def solve(array):
    global best, combs, tops
    rows = list(x for x in range(len(array)))
    columns = len(array[0])
    top = 0
    tops = list([0] * columns)
    for x in range(0, columns):
        for y in rows:
            if array[y][columns - x - 1] > top:
                top = array[y][columns - x - 1]
        tops[x] = top + tops[x - 1]
        top = 0
    tops.reverse()
    print(tops)

    combs = np.zeros(columns, dtype=np.int16)
    visit(array, rows, columns, 0)
    print("best is: ", c.best)
    print(sum(c.best))


def visit(array, rows, columns, column):
    global c, combs, tops
    if column == columns:
        return
    for row in rows:
        new_rows = rows.copy()
        combs[column] = array[row][column]
        if combs[-1] != 0:
            check = np.sum(combs)
            if check >= c.best_sum:
                c.best = np.array(combs)
                c.best_sum = check
        else:
            check = np.sum(combs)
            if c.best_sum > check + tops[column + 1]:
                continue

        new_rows.remove(row)
        visit(array, new_rows, columns, column + 1)
        combs[column] = 0


solve(array1)
