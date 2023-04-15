#personal data
#professional data

#fnmae,lname,age,location

#professional data ===id,prof,salary


#id,fname,lname,age,location,salary

class Personal_data:
    def printPersonal_data(self,fname,lname,age,location):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.location=location

class Professional_data(Personal_data):
    def printProfessional_data(self,id,proff,salary):
        self.id=id
        self.proff=proff
        self.salary=salary
        print(self.id,self.fname,self.lname,self.age,self.location,self.proff,self.salary)
employee1=Professional_data()
employee1.printPersonal_data('venu','k',22,'kochi')
employee1.printProfessional_data(101,'analyst',20000)

