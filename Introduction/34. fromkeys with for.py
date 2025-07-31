myList = ['sorena', 'bahram', 'ali', 'amir']
vehicle = ['car', 'motor', 'bike']

myDict = dict.fromkeys(myList, vehicle)
for key, value in myDict.items():
    print(key, value)
    

# answer = sorena ['car', 'motor', 'bike']
#          bahram ['car', 'motor', 'bike']
#          ali ['car', 'motor', 'bike']   
#          amir ['car', 'motor', 'bike']  