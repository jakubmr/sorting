#Quicksort iterative version for random pivot

import time
from converter import convertedList
from random import randint

def quickSortIterativeRandom(list):
    convList = convertedList(list)

    start = time.time()

    p = 0
    r = len(convList) - 1

    stack = []
    stack.append(p)
    stack.append(r)

    while len(stack) > 0:

        r = stack.pop()
        p = stack.pop()

        x = partition_r(convList, p, r)

        if x - 1 > p:
            stack.append(p)
            stack.append(x - 1)

        if x + 1 < r:
            stack.append(x + 1)
            stack.append(r)

    end = time.time()

    return end - start, convList

def partition_r(list, p, r):
    x = randint(p, r)
    list[x], list[r] = list[r], list[x]

    i = (p - 1)
    pivot = list[r]

    for j in range(p, r):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[r] = list[r], list[i+1]
    return (i + 1)
