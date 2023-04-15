class Student:
    college='SDC'   #====> college name static au so elladom auto fill akum
    def setvalue(self, fname,lname,age,course):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course

    def printvalue(self):
        print(self.fname,self.lname,self.age,self.course,Student.college)   #college name print cheyan class name.college Add cheynm

Student1=Student()
Student1.setvalue('abhay','a',21,'data science')
Student1.printvalue()

Student2=Student()
Student2.setvalue("ramu",'kp',20,'flutter')
Student2.printvalue()

Student3=Student()
Student3.setvalue('gopu','s',55,'angular')
Student3.printvalue()

Student4=Student()
Student4.setvalue('mahi','kp',32,'flutter')
Student4.printvalue()

Student5=Student()
Student5.setvalue("abhi",'a',44,'django')
Student5.printvalue()