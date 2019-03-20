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
    return (end - start, convList)

print("IS sorting time: {}".format(insertionSort("random 1000.txt")[0]))
print(insertionSort("random 1000.txt")[1])
