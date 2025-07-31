class MyClass:
    # def __init__(self, file1, file2):
    #     self.file1 = file1
    #     self.file2 = file2

    def myFunc(file1, file2):
        with open(file1) as f1, open(file2, 'w') as f2:
            text = f1.read()
            l = 0
            u = 0
            for char in text:
                if char.islower():
                    l +=1
                else:
                    u += 1
            f2.write(f'Number of lower characters = {l} , \nNumber of upper characters = {u}')
            
MyClass.myFunc('61. filling.txt','62. filling(2).txt')