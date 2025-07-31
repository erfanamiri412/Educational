class Employee:
    def __init__(self, name, family, code, s1):
        self.name = name
        self.family = family
        self.code = code
        self.s1 = s1

    def showInfo(self):
        return f'name = {self.name}, family = {self. family}, code = {self.code}, salary 1 = {self.s1}'
    
class Programmer(Employee): # single level inheritance
    def __init__(self, name, family, code, s1, s2):
        Employee.__init__(self, name, family, code, s1)
        self.s2 = s2

    def showInfo(self): # method overriding   
        return Employee.showInfo(self)+ ', salary 2 = '+str(self.s2)
    
class PythonProgrammer(Programmer):
    def __init__(self, name, family, code, s1, s2, s3):
        Programmer.__init__(self, name, family, code, s1, s2)
        self.s3 = s3

    def showInfo(self):
        return Programmer.showInfo(self)+'salary 3 ='+ str(self.s3)