class Calculation:
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def sub(x,y):
        return x - y
    
    @classmethod
    def mul(cls,x,y):
        return x*y
    
    @classmethod
    def div(cls,x,y):
        if y!=0:
            return x/y
        
print(Calculation.add(10,20))
print(Calculation.sub(10,20))
print(Calculation.mul(10,20))
print(Calculation.div(10,20))

# answer = 30
#         -10
#         200
#         0.5