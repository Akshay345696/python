class  Calculation1:
    def Summation(self,a,b):
        return a+b;
class Calculation(self,a,b):
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation,Calculation2):
    def Divide(self,a,b):
        return a/b;

d = Derived()
d.Summation(10,20)
d.Multiplication(10,20)
d.Divide(10,20)