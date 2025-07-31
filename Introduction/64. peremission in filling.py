try:
    with open('61. filling.txt') as f:
        print(f.read())
except PermissionError:
    print(PermissionError)

# answer = Hello world!
#          1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10        
#          A bullet that is fired, never returns to gun.