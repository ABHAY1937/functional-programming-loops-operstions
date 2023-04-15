f=open("fruits",'r')
f1=open("coping fruits",'w')

for i in f:
   data=i.rstrip('\n')
   if data != "apple":
        f1.write(i)