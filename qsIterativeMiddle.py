import time
from converter import convertedList

def quickSortIterativeMiddle(list):
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
            i = l - 1
            j = p + 1
            x = convList[(l + p) // 2]

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
