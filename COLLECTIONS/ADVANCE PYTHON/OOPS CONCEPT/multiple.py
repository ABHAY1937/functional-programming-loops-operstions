#class person
    #fname,lname,age

#class employee
   #id,prof,salary

#class contact
   #phno,sex,location

#id,fnmae,lname,age,prof,salary,phno,sex,location
class Person:
    def printperson(self,fname,lname,age):
        self.fname=fname
        self.lnamr=lname
        self.age=age
class Employee:
    def printemployee(self,id,prof,salary):
        self.id=id
        self.prof=prof
        self.salary=salary
class Contact(Person,Employee):
    def printcontact(self,phno,sex,location):
        self.phno=phno

        self.sex=sex
        self.location=location
        print(self.id,self.fname,self.lnamr,self.age,self.prof,self.salary,self.phno,self.sex,self.location)
obj1=Contact()
obj1.printperson('abhi','a',22)
obj1.printemployee(101,'scientist',200000)
obj1.printcontact(12345678910,'male','kochi')
