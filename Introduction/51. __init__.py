class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
    
    def __str__(self):
        return f'hello {self.name}'
    
p1 = Person('ali', 'mohammadi', 20)
print(p1)

# answer = hello ali