#Converter for string from file to the list
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
