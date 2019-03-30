#Insertion sort

import time
from converter import convertedList

def insertionSort(list):
    convList = convertedList(list)
    start = time.time()
    for j in range(1, len(convList)):
        key = convList[j]

        i = j - 1
        while (i >= 0) and (convList[i] > key):
            convList[i + 1] = convList[i]
            i -= 1
        convList[i + 1] = key
    end = time.time()
    return end - start, convList
