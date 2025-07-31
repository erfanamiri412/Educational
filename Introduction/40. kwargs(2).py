def f(**kwargs):
    avg = sum(kwargs.values())/len(kwargs.values())
    c = 0
    for value in kwargs:
        if value > avg :
            c+=1
    return f'number of marks greater than average : {c}'

myDict = dict()
n = int(input('Enter number of keys, values: '))
for i in range(n):
    myDict.update({input(f'Enter name {i+1}: '): float(input(f'Enter grade {i+1}: '))})
print(f(**myDict))