#dictionary

#key_value pair

#id:101
#fname:vinay
#lname:kp
#age:25
#saslary:1000

#key :id,fname,lname,age,salary
#values : 101,vinay,kp,25,1000

#how to define?
dic={}
print(type(dic))

dic1={'id':101,"fname":'vinay','lname':"kp",'age':25,'salary':1000,True:False}
print(dic1)
#supports hetrogenious property

dic={'id':101,"fname":'vinay','lname':"kp",'age':25,'age':27}
print(dic)   # does not suppot duplicate keys

dic2={'id':101,"fname":'vinay','lname':"kp",'age':25,'marks':25}
print(dic2)
#support duplicate values
#insertion order preserved
# dictionay is mutable

# define    hetro    insertion oreder     duplicate             mutable\imutable
#list []      yes      preserved          yes                      mutable
#tuples ()     yes       preserved        yes                     imutable
#set   set()    yes     not preserved     no                      mutable
#dictionary{}    yes       preserved      key:no, values:yes      mutable