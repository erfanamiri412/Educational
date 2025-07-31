list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.reverse()
print(list1)

# answer = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[::-1])

# answer = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in reversed(list1):
    print(i, end = " ")

# answer = 10 9 8 7 6 5 4 3 2 1