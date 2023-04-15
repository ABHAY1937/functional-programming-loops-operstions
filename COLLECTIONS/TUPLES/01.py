tu=(10,20,30,40,50,60,70,80,90,100)

#30=====> 150

#tuple is imutable

lst=list(tu)
lst[2]=150
print(lst)

tu=tuple(lst)
print(tu)