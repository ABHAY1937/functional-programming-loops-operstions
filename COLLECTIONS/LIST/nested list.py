#Nested list

lst=[[101,'arjun','m',30,'big_data',1500,],
     [102,'arun','b',31,'python',12000],
     [103,'abhay',"m",22,"Data_Scientist",1000000],
     [104,'vinod','m',32,'flutter',1000]]
print(lst)
for i in lst:
     print(i) #===> if we aplly a for loop in a nested list we can seperate the values in different lines jst by
     # using a loop (i)

#age above 28 details
for i in lst:

  if i[3]>28:
     print(i)

# age above 29 fname,lname,age,proffesion

for i in lst:
     if i[3]>29:
          print(i[1],i[3],i[4])
      #or this can ba used
     # print(i[1:5])

#prof bigdata fnmae lastname age
for i in lst:
     if i[4]=='bigdata':
          print(i[1:4])

#prof python fname, lname,age profession salery
for i in lst:
     if(i[4]=='python'):
          print(i[1:])
#bigdata and age above 29
# fname  age salery

for i in lst:
     if(i[4]=="big_data" and i[3]>29):
          print(i[1::2])

#salary above 1750 and proffesion python
# fnmae lname age
for i in lst:
     if(i[5]>1750 and i[4]=='python'):
          print(i[1:4])

#total salary of all people
sum=0
for i in lst:
     sum+=i[-1]
print(sum)         #=====>note this some complicated


