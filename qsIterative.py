#Quicksort iterative version for pivot at the beginning and at the end
#Default pivot value: 'start'
#Examples:
#quickSortIterative(list)
#quickSortIterative(list, 'end')

import time
from converter import convertedList

def quickSortIterative(list, pivot = 'start'):
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

        x = partition(convList, p, r, pivot)

        if x - 1 > p:
            stack.append(p)
            stack.append(x - 1)

        if x + 1 < r:
            stack.append(x + 1)
            stack.append(r)

    end = time.time()

    return end - start, convList

def partition(list, p, r, pivot):

    # pivot at the beginning
    if pivot == 'start':
        i = (p + 1)
        x = list[p]

        for j in range(p + 1, r + 1):
            if list[j] < x:
                list[i], list[j] = list[j], list[i]
                i += 1
        list[i-1], list[p] = list[p], list[i-1]
        return (i - 1)

    # pivot at the end
    if pivot == 'end':
        i = (p - 1)
        x = list[r]

        for j in range(p, r):
            if list[j] <= x:
                i += 1
                list[i], list[j] = list[j], list[i]
        list[i+1], list[r] = list[r], list[i+1]
        return (i + 1)
