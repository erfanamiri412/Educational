myList = [10, 15, 20, 25, 30]
def f(myList):
    for i in myList:
        if i%2==0:
            print(i)
print(list(map(lambda x: x%2==0, myList)))

# answer = [True, False, True, False, True]