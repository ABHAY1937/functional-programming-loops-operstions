#list comprehension
#convert any progems in list to a single line programme

#no syntax

#method1
#method2
#method3

#empty list ====> 1 to 50

lst=[]
for i in range(1,51):
    lst.append(i)
print(lst)

#method1
#variabl_name=[print range]
#1 to 30 elements
lst1=[i for i in range(1,31)]
print(lst1)


#1 to 25 elemets square
lst2=[i**2 for i in range(1,26)]
print(lst2)

#add 3 in lst
lst=[1,2,3,4,5,6,7,8,9,10]
lst3=[i+3 for i in lst]
print(lst3)

#method2 ====> its aplicable for conditions only
#1 to 25 range even numbers
#syntax
#[print range condition]
lst4=[i for i in range(1,26) if (i%2==0)]
print(lst4)

#1 to 50 range odd numbers
lst5=[i for i in range(1,51) if(i%2 != 0)]
print(lst5)

#1 to 30 range even no square (2,4) .....
lst6=[(i,i**2) for i in range(1,31) if(i%2==0)]
print(lst6)

#1 to 100 range divisible by 5
lst7=[i for i in range(1,101) if i%5==0]
print(lst7)

#1 to 10 range
#1,1,2
#2,4,3
#3,9,4
#4,16,5
#5,25,6


#10,100,11

lst8=[(i,i**2,i+1) for i in range(1,11) ]
print(lst8)

#
string='luminartechnolab'
#string vowels
vowels='aeiou'
lst9=[i for i in string if i in vowels]
print(lst9)
