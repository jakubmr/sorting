from random import randint

def randomListNumbers(size):
    return [randint(0, size*10) for i in range(size)]

def aShapeListNumbers(size):
    t = []
    for i in range(size//2):
        t.append(i)
    for i in range(size//2, -1, -1):
        t.append(i)
    return t

def vShapeListNumbers(size):
    t = []
    for i in range(size//2, 0, -1):
        t.append(i)
    for i in range(0, (size//2)+1):
        t.append(i)
    return t

def listOfNumbers(size):
    return list(range(size))

def reverseListOfNumbers(size):
    return sorted(list(range(size)), reverse = True)
