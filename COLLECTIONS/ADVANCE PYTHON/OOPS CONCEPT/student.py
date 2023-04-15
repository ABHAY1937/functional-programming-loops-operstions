#student
#id,fnmae,lname,age,course,colegename
#5 object
          #VARIABLE
# 2 type of variables are available
#1. static varable
#2.dynamic variable or instance variable
class Student:
    def setvalue(self, fname,lname,age,course,college_name):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
        self.college_name=college_name
    def printvalue(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.course)
        print(self.college_name)

Student1=Student()
Student1.setvalue('abhay','a',21,'data science','luminar')
Student1.printvalue()

Student2=Student()
Student2.setvalue("ramu",'kp',20,'flutter','brocamp')
Student2.printvalue()

Student3=Student()
Student3.setvalue('gopu','s',55,'angular','gb c')
Student3.printvalue()

Student4=Student()
Student4.setvalue('mahi','kp',32,'flutter','abc college')
Student4.printvalue()

Student5=Student()
Student5.setvalue("abhi",'a',44,'django','bcd college')
Student5.printvalue()