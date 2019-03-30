#Heapsort

import time
from converter import convertedList

def buildHeap(list):
    heapsize = len(list)
    for i in range(heapsize//2, -1, -1):
        heapify(list, i, heapsize)

def heapify(list, i, heapsize):
    l = (2 * i) + 1
    r = (2 * i) + 2
    if (l < heapsize) and (list[l] > list[i]):
        largest = l
    else:
        largest = i
    if (r < heapsize) and (list[r] > list[largest]):
        largest = r
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        heapify(list, largest, heapsize)

def heapSort(list):
    convList = convertedList(list)
    start = time.time()
    buildHeap(convList)
    heapsize = len(convList)
    for i in range((len(convList) - 1), 0, -1):
        convList[0], convList[i] = convList[i], convList[0]
        heapsize -= 1
        heapify(convList, 0, heapsize)
    end = time.time()
    return end - start, convList
