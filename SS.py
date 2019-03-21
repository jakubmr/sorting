import time

#converting string into list
def convertedList(name):
    t = []
    f = open("numbers generator/lists/" + name, "r")
    c = f.read().replace("[", "").replace("]", "").split(",")
    f.close()
    for i in c:
        i.lstrip()
        if i.lstrip().isdigit():
            t.append(int(i.lstrip()))
    return t

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

print(selectionSort('random 8000.txt'))
