import time
from converter import convertedList

def selectionSort(list):
    convList = convertedList(list)
    start = time.time()
    for j in range(len(convList) - 1, 0, -1):
        max = j
        for i in range(j - 1, -1, -1):
            if convList[i] > convList[max]:
                max = i
        convList[j], convList[max] = convList[max], convList[j]
    end = time.time()
    return end - start, convList
