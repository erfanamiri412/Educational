myList = [10, 15, 20, 25, 30]
def f(myList):
    for i in myList:
        if i%2==0:
            print(i)
print(list(filter(lambda x: x%2==0, myList)))

# answer = [10, 20, 30]