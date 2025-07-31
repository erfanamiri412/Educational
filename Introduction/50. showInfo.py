class Person:
    name = 'ali'
    family = 'bangi'
    age = 16

    def showInfo(self):
        return f'name : {self.name}, family : {self.family}, age : {self.age}'

p1 = Person()
print(p1.showInfo())

# answer = name : ali, family : bangi, age : 16