#Tuples

#properties
# 1.How to define

tu=()
print(type(tu))

tu1=tuple()
print(type(tu1))

#2.hetrogenious data suported or not
tu=(20,40,50.000002,1223123556,True,False)
print(tu)   #====>it supports hetrogenious

#3.Duplicate values
tu=(2,2,2,True)
print(tu) #supports duplcates

#4.Insertion value preserved or not
tu=(20,40,50.000002,1223123556,True,False)
print(tu)  #=====> insertion order preserved

#5.mutable or imutable
tu=(10,15,20,4,2,45,66,332,2)
tu[2]=100
print(tu)   #========> it is imutable
# we cannot change the values in tuples