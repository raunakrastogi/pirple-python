# Homework Assignment 4 Lists

myUniqueList = []
myLeftOvers = []

def Add(element):
    if element in myUniqueList:
        addRejects(element)
        return False
    else:
        myUniqueList.append(element)
        return True

def addRejects(element):
    myLeftOvers.append(element)


print(Add("sun"))
print(myUniqueList)
print(myLeftOvers)

print(Add("moon"))
print(myUniqueList)
print(myLeftOvers)

print(Add("moon"))
print(myUniqueList)
print(myLeftOvers)