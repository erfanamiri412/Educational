myTuple = (10, 20, 30, 50, 60)
myList = list(myTuple)
myList[3] = 40
myTuple = tuple(myList)
print(myTuple)

# answer = (10, 20, 30, 40, 60)