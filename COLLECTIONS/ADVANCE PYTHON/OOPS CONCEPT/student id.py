#student
#id,fname,lname,age,course,collegename

#perfomance
#sub1 mark,sub2 mark,sub3 mark,grade


#id,fname,lname,age,course,sub1,sub2,sub3,grade,college name

class Student:
    College='GHSS '
    def printstudent(self,id,fname,lname,age,course):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.course=course
class Performance(Student):
    def printPerformence(self,sub1_mark,sub2_mark,sub3_mark,grade):
        self.sub1_mark=sub1_mark
        self.sub2_mark=sub2_mark
        self.sub3_mark=sub3_mark
        self.grade=grade
        print(self.id,self.fname,self.age,self.course,self.sub1_mark,self.sub2_mark,self.sub3_mark,self.grade,Student.College)
obj1=Performance()
obj1.printstudent(101,'thenj','A',12,'science')
obj1.printPerformence(30,40,50,'B')





