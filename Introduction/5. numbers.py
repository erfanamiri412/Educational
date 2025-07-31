numbers = []
odd = []
even = []
n = int(input('Enter amount of nembers: '))
for i in range (n):
    numbers.append(int(input(f'Enter number{i+1}: ')))
    for i in numbers:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
print(even, odd)