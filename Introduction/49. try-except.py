try:
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    print(x/y)
except ValueError:
    print('invalid input')
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('error!')
else :
    print('finished')