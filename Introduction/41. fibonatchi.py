def fib(n):
    a = 0
    b = 1
    if n<0:
        return 'error!'
    elif n==0 or n==1:
        return n
    else :
        for i in range(1,n):
            c = a+b
            a = b
            b = c
        return c
        
print(fib(10))

# answer = 55