lst=[1,2,3,4,5,6,7,8,9,10]
#each elements square

def square(num):
    return num**2
lst1=list(map(square,lst))
print(lst1)


#
lst1=list(map(lambda num:num**2 ,lst))
print(lst1)

#cube of a number
lst2=list(map(lambda num:num**3,lst))
print(lst2)

#find even numbers
lst3=list(filter(lambda num:num%2==0 ,lst))
print(lst3)

#find odd number and its square
lst4=list(filter(lambda num:num%2 !=0 ,lst))
lst5=list(map(lambda num:num**2,lst4))
print(lst5)

