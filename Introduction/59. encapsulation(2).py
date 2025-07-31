class Person:
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, a):
        if 18 < a < 80:
            self.__age = a
        else:
            self.__age = 0

    @age.deleter
    def age(self):
        del self.__age

p1 = Person()
print(p1.age)
p1.age = 20
del p1.age
print(p1.age)