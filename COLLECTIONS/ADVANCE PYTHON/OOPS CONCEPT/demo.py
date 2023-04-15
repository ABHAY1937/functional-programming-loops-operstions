class Person:
    def setvalue(self, fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location
    def printvalue(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.location)
Person1=Person()
Person1.setvalue('abhay','a',21,'tvm')
Person1.printvalue()
