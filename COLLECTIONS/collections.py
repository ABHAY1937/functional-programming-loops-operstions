#collection of hetrogenious data is known as collections

#in array we can store only one type of data type and the size is limited to overcome this we use collections

#there are 4 types of collections
#1.List
#2.tuples
#3.set
#4.Dictionary


#properties
#1.How to define ?

#2. Hetrogenous data supported or not ?

#3. Duplicates values are supported or not ?
#list=[3,4,5,4,3,2]

#4. Insertion order is preserved or not ?
#eg==>[1,2,3,4,5,6,7,8,9]=[1,2,3,4,5,6,7,8,9]
#[1,2,3,4,,5,67,8,,9,9]=[8,76,5433,,,2,,]

#5. Mutable or imutable
#[1,5,10,15,20] ====> 20 ===>100

lst=[10,20,30,40,50,60,10,20,30,40]
print(lst ) #insertion order is preserved

# for collecting a particular value in a list we use a term as :
# index
# values starts from 0 to (n-1)

print(lst[3])
print(lst[7])
print(lst[5])

#mutable or immutable checking
lst[3]=1000
lst[5]=999
print(lst)  #list is mutable