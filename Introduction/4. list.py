myList = []
for i in range(5):
    myList.append(int(input(f'Enter number{i+1}')))
for i in myList:
    if i%2==0:
        print(i, end=', ')