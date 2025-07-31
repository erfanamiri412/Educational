def f(lst): # generator function
    for i in lst:
        if i%2==0:
            yield i

myList = [10, 15, 20, 25, 30]
print(list(f(myList)))
print(tuple(f(myList)))
for i in f(myList):
    print(i)

# answer = [10, 20, 30]
#          (10, 20, 30)
#          10
#          20
#          30