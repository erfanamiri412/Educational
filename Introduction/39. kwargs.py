def f(**kwargs):
    for key,value in kwargs.items():
        return key, value

myDict = {}
n = int(input('Enter number of keys, values: '))
for i in range(n):
    myDict.update({(input(f'Enter key{i+1}:')):input(f'Enter value{i+1}: ')})
print(f(**myDict))