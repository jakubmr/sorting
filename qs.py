import time
from converter import convertedList
import sys
sys.setrecursionlimit(8000)

def mainQuickSort(list):
    convList = convertedList(list)
    start = time.time()
    quickSort(convList, 0, len(convList) - 1)
    end = time.time()
    return end - start, convList

def quickSort(list, p, r):
    if p < r:
        q = partition(list, p, r)
        quickSort(list, p, q)
        quickSort(list, q + 1, r)

def partition(list, p, r):
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
