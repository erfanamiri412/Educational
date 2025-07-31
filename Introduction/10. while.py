myList = [10, 20, 30, 20, 40, 20, 50]
while 20 in myList:
    myList.remove(20)
print(myList)

# answer = [10, 30, 40, 50]

myList = [10, 20, 30, 20, 40, 20, 50]
myList2 = []
for i in myList:
    if i not in myList2:
        myList2.append(i)
print(myList2)

# answer = [10, 20, 30, 40, 50] 