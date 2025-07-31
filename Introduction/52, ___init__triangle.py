from math import pi

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        a = self.r**2*pi
        return f'area = {a:0.2f}'
    
    def perimeter(self):
        p = self.r*2*pi
        return f'perimeter = {p:0.2f}'
    
c1 = Circle(10)
print(c1.area())
print(c1.perimeter())

# answer = area = 314.16
#          perimeter = 62.83