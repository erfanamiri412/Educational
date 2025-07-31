list1 = ['reza', 'ali', 'amir', 'mohammad']
list2 = [100, 90, 80, 70, 60]
list3 = [50, 40, 30, 20, 10]
print(list(zip(list1, list2, list3)))
print(tuple(zip(list1, list2, list3)))

# answer = [('reza', 100, 50), ('ali', 90, 40), ('amir', 80, 30), ('mohammad', 70, 20)]
        #  (('reza', 100, 50), ('ali', 90, 40), ('amir', 80, 30), ('mohammad', 70, 20))    