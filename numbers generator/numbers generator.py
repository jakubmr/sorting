from random import randint

def randomListNumbers(size, name = "random"):
    f = open(f"numbers generator/lists/{name} {size}.txt", "w+")
    f.write(str([randint(0, size*10) for i in range(size)]))
    f.close()
    #return [randint(0, size*10) for i in range(size)]

def aShapeListNumbers(size, name = "aShape"):
    t = []
    for i in range(size//2):
        t.append(i)
    for i in range(size//2, -1, -1):
        t.append(i)
    f = open(f"numbers generator/lists/{name} {size}.txt", "w+")
    f.write(str(t))
    f.close()
    #return t

def vShapeListNumbers(size, name = "vShape"):
    t = []
    for i in range(size//2, 0, -1):
        t.append(i)
    for i in range(0, (size//2)+1):
        t.append(i)
    f = open(f"numbers generator/lists/{name} {size}.txt", "w+")
    f.write(str(t))
    f.close()
    #return t

def listOfNumbers(size, name = "ordinary"):
    f = open(f"numbers generator/lists/{name} {size}.txt", "w+")
    f.write(str(list(range(size))))
    f.close()
    #return list(range(size))

def reverseListOfNumbers(size, name = "reverse"):
    f = open(f"numbers generator/lists/{name} {size}.txt", "w+")
    f.write(str(sorted(list(range(size)), reverse = True)))
    f.close()
    #return sorted(list(range(size)), reverse = True)

for i in range(1000, 8500, 500):
    randomListNumbers(i)
    aShapeListNumbers(i)
    vShapeListNumbers(i)
    listOfNumbers(i)
    reverseListOfNumbers(i)
