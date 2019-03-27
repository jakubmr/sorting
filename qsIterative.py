import time
from converter import convertedList

def quickSortIterative(list, pivot = 'middle'):
    convList = convertedList(list)

    start = time.time()

    p = 0
    r = len(convList) - 1

    size = r - p + 1
    stack = [0] * size

    top = -1

    top += 1
    stack[top] = p
    top += 1
    stack[top] = r

    while top >= 0:

        r = stack[top]
        top -= 1
        p = stack[top]
        top -= 1

        x = partition(convList, p, r, pivot)

        if x - 1 > p:
            top += 1
            stack[top] = p
            top += 1
            stack[top] = x - 1

        if x + 1 < r:
            top += 1
            stack[top] = x + 1
            top += 1
            stack[top] = r

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

    # pivot in the middle (default value)
    if pivot == 'middle':
        x = list[(p + r) // 2]
        i = p - 1
        j = r + 1
        while True:
            while True:
                j -= 1
                if list[j] <= x:
                    break
            while True:
                i += 1
                if list[i] >= x:
                    break
            if i < j:
                list[i], list[j] = list[j], list[i]
            else:
                return j

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

# print(quickSortIterative('random 6000.txt', 'start')[0])
# print(quickSortIterative('random 6000.txt')[0])
# print(quickSortIterative('random 6000.txt', 'end')[0])
