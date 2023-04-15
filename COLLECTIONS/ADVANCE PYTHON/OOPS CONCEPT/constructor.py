#Constructor

#class
  #constructor

#object(values)

class Person:
    def __init__(self,fname,lname,age,phno):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.phno=phno
    def printvalue(self):
        print(self.fname,self.lname,self.age,self.phno)
Person1=Person('abhay','a','21','1212121212')
Person1.printvalue()
Person2=Person('vovo','kp',32,333222555)
Person2.printvalue()