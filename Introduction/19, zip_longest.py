from itertools import zip_longest
list1 = ['reza', 'ali', 'amir', 'mohammad', 'parsa', 'sadegh']
list2 = [100, 90, 80, 70, 60]
list3 = [50, 40, 30, 20, 10]
print(list(zip_longest(list1, list2, list3)))
for i in zip_longest(list1, list2, list3):
    print(i)

# answer = [('reza', 100, 50), ('ali', 90, 40), ('amir', 80, 30), ('mohammad', 70, 20), ('parsa', 60, 10), ('sadegh', None, None)]
        #  ('reza', 100, 50)
        #  ('ali', 90, 40)
        #  ('amir', 80, 30)
        #  ('mohammad', 70, 20)
        #  ('parsa', 60, 10)
        #  ('sadegh', None, None)

from itertools import zip_longest
list1 = ['reza', 'ali', 'amir', 'mohammad', 'parsa', 'sadegh']
list2 = [100, 90, 80, 70, 60]
list3 = [50, 40, 30, 20, 10]
print(list(zip_longest(list1, list2, list3)))
for i in zip_longest(list1, list2, list3, fillvalue='*'):
    print(i)

# answer = [('reza', 100, 50), ('ali', 90, 40), ('amir', 80, 30), ('mohammad', 70, 20), ('parsa', 60, 10), ('sadegh', None, None)]    #          ('reza', 100, 50)
#          ('ali', 90, 40)
#          ('amir', 80, 30)
#          ('mohammad', 70, 20)
#          ('parsa', 60, 10)
#          ('sadegh', '*', '*')