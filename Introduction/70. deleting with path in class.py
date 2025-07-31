import os
class MyClass:
    def __init__(self, file):
        self.file = file

    def delete_file(self):
        if os.path.exists(self.file):
            os.remove(self.file)
        else:
            print('ffile not found')
    
mc1 = MyClass('filling.txt')
mc1.delete_file()