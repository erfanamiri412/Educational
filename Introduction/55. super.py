class Employee:
    def __init__(self, name, family, code, s1):
        self.name = name
        self.family = family
        self.code = code
        self.s1 = s1

    def showInfo(self):
        return f'name = {self.name}, family = {self. family}, code = {self.code}, salary 1 = {self.s1}'
    
class FreeLancer(Employee):
    def __init__(self, name, family, code, s1, s2):
        super().__init__(name, family, code, s1)
        self.s2 = s2

    def showInfo(self):
        return f'code = {self.code}, name = {self.name}, family = {self.family}, salary 1 = {self.s1}, salary 2 = {self.s2}'