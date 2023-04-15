f=open('numbers','r')
lst=[]
for i in f:
   lst.append(int(i.rstrip('\n')))
print(lst)
print(sum(lst))
#append all the values in a lst and find its total sum

#strip ====>for remove a value
#rstrip ===> for removing value from right
#lstrip ====>for removing value from left
#eg===>
# data='hello\n'
# data1=data.rstrip('o\n')
# print(data1)

