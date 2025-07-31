def f(*args):
    even = 0
    odd = 0
    for i in args:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return f'odd = {odd}, even = {even}'

myList = []
n = int(input('Enter amount f numbers: '))
for i in range(n):
    myList.append(int(input('Enter number: ')))
print(f(*myList))