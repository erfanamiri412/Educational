with open('filling.txt', 'r+') as f:
    f.tell()                           # موقعیت مکان نما را مشخص میکند
    f.seek(0)                          # موقعیت مکان نما را طبق خواسته ما تغییر میدهد
    f.write('Hello! ')
    print(f.read())