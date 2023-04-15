# empty list
# add 1to 50
# even num lst
# odd num lst

#list sum
#even list sum
# odd list sum

lst=[]
lst1=[]
lst2=[]
for i in range(1,51):
    lst.append(i)
print(lst)
for i in range(1,51):
    if(i%2==0):
     lst1.append(i)
print(lst1)
for i in range(1,51):
    if(i%2!=0):
         lst2.append(i)
print(lst2)

print(sum(lst))

print(sum(lst1))

print(sum(lst2))
