class MyClass:
    def myFunc(self, file1, file2):
        with open(self.file1) as f1, open(self.file2, 'a') as f2:
            text = f1.read()
            words = text.split()
            even = 0
            odd = 0
            for word in words:
                if word.isnumeric():
                    if int(word)%2==0:
                        even += 1
                    else :
                        odd += 1
            f2.write(f'Number of even numbers = {even}, number of odd numbers = {odd}')

MyClass.myFunc('61. filling.txt','62. filling(2).txt')