import math
a = int(input (" enter the 1st number :"))
b = int(input (" enter the 2nd number :"))
c = int(input (" enter the 3rd number :"))  
class QuadraticEquation:   
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return (self.b ** 2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + math.sqrt(self.discriminant())) / (2 * self.a)

    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - math.sqrt(self.discriminant())) / (2 * self.a)
        
eq = QuadraticEquation(a,b,c)
nn=print(eq)
print(nn)
r1 = eq.root1()
r2 = eq.root2()
