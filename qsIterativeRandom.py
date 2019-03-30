import time
from converter import convertedList
from qsIterative import quickSortIterative
from qsIterativeMiddle import quickSortIterativeMiddle
from random import randint

# def qsIterativeRandom(list):
#     convList = convertedList(list)
#
#     x = randint(0, len(convList) - 1)
#
#     if x == 0:
#         return x, quickSortIterative(list, 'start')
#
#     elif x == len(convList) - 1:
#         return x, quickSortIterative(list, 'end')
#
#     else:
#         return x, quickSortIterativeMiddle(list)


def quickSortIterativeRandom(list):
    convList = convertedList(list)

    start = time.time()

    l = 0
    p = len(convList) - 1
    stack1, stack2 = [], []

    stack1.append(l)
    stack2.append(p)

    while len(stack1) > 0 and len(stack2) > 0:
        l = stack1.pop()
        p = stack2.pop()

        while l < p:
            r = randint(l, p)
            if r == l:
                r += 1
            elif r == p:
                p -= 1
            list[p], list[r] = list[r], list[p]
            x = list[p]
            i = l - 1
            j = p + 1
            #x = randint(l, p)

            #x, p = p, x
            #x = convList[(l + p) // 2]

            while i <= j:

                while True:
                    j -= 1
                    if convList[j] <= x:
                        break

                while True:
                    i += 1
                    if convList[i] >= x:
                        break

                if i <= j:
                    convList[i], convList[j] = convList[j], convList[i]
            if i < p:
                stack1.append(i)
                stack2.append(p)
            p = j

    end = time.time()
    return end - start, convList


print(quickSortIterativeRandom('aShape 4000.txt'))
