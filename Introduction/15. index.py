myList = [10, 20, 30, 20, 40, 20, 50]
print(myList.index(20))

# answer = 1 -> first place in list

myList = [10, 20, 30, 20, 40, 20, 50]
for i in range(len(myList)):
    if myList[i]==20:
        print(i)

# answer = 1,1,3,5