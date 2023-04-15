import function1.operation
data=function1.operation.add(60,70)
print(data)

block=function1.operation.sub(30,20)
print(block)

chain=function1.operation.multi(20,10)
print(chain)

data1=function1.operation.div(30,5)
print(data1)

#drawback is always we have to add module name and package in it that is gone be a big problem
#to over come tis we intrduce a new metod called its syntax is
# [ from package_name.modulename import * ]

from function1.operation import *
data=add(20,30)
print(data)

data1=sub(60,30)
print(data1)

data2=multi(20,2)
print(data2)

data3=div(90,10)
print(data3)