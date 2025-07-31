class Person:
    name = 'hossein'          # public
    _family = 'jahan bakhsh'  # protected
    __age = 16                # private

    def __show(self):         # private method
        print('hello')

p1 = Person()
print(p1.name)
print(p1._family)
print(p1.__age)               # private
p1._Person__show()