x = int(input('Enter value: '))
y = int(input('Enter value: '))
z = int(input('Enter value: '))
if x==z==y:
    print('equilateral')
elif x==y!=z:
    print('isoceles')
elif x**2 + y**2 == z**2 or x**2 + z**2 == y**2 or y**2 + z**2 == x**2:
    print('right')
elif x!=y!=z:
    print('scalene')