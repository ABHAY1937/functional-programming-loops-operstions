#multiple inheritence

class A:
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)
class B:
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2)
class C(A,B):
    def printc(self,num3):
        self.num3=num3
        print("inside class C",self.num3)

obj1=C()
obj1.printc(19)
obj1.printb(20)
obj1.printa(10)