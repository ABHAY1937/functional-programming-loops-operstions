#employee
#id,fname,lname,age ,prof ,salary,compny name

class Employee:
    companyname='IBM'
    def setvalue(self,id,fname,lname,age,prof,salary):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.salary=salary
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.salary,Employee.companyname)
Employee1=Employee()
Employee1.setvalue(101,'sabu','ms',22,'develper',200000)
Employee1.printvalue()

Employee2=Employee()
Employee2.setvalue(102,'abhishek','mn',23,'tester',100000)
Employee2.printvalue()

Employee3=Employee()
Employee3.setvalue(1001,'sabu','ms',25,'mern develper',200000)
Employee3.printvalue()

Employee4=Employee()
Employee4.setvalue(1002,'abhishek','mn',53,'software tester',100000)
Employee4.printvalue()