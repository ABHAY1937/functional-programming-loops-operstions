f=open("C:/Users/Dell/Documents/.unknown",'r')
for i in f:
  data=i.rstrip('\n').split(",")

#country india fname,lanme,age prof

#1. age above 50 fname lname age prof
  if data[3] > '50':
      print(data[1:5])

#pilot fname l mname age prof country
  if data[4]=='Piolet':
    print(data[1:])

#working profession piolet and age above50
  if data[3]>'50'and data[4]=='Piolet':
    print(data[1:])
#us and age above 50 fname, lname, age prof location
 if data[-2]=='us' and data[3]>'50':
   print(data[1:])




