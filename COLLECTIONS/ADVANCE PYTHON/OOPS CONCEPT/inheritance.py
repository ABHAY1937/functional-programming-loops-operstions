#inheritence

#class 1

    #methode \instance_value

#class2

  #single inheritence

  # 1 parent class
  # 1 child class

class A:             #parent class/base class/superclass
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)

class B(A): #child class/sub class/derived class
    def printb(self,num2):
        self.num2=num2
        print("inside class B",self.num2)
obj1=B()
obj1.printb(19)
obj1.printa(20) #classA
