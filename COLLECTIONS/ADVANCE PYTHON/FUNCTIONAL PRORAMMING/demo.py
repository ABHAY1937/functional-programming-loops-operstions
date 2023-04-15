#1.lst=[5,6,7,8,9,10]  #exact list

#1 create a identical list

#2.each element add by 2

#3.square  value above 50 data print

lst=[5,6,7,8,9,10]
lst1=[i for i in lst]
print(lst1)

lst1=list(map(lambda num:num+2 ,lst))
print(lst1)

lst=[i**2 for i in lst if i**2>50 ]
print(lst)

