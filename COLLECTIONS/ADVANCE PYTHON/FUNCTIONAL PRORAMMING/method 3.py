#method 3 :more than one condition

#1 to 30 even sum odd square
#[print1 if condition1 else print2 range]
#[print1 if condition1 else print 2 if condition2 else print3 range]


#1 to 50 elements even square odd cube

#elements

#(1,1),(2,4),(3,27)..............
list=[(i,i**2)  if i%2==0 else (i,i**3) for i in range(1,51) ]
print(list)


#1 to 30 even ===>even  odd===>odd
#element
#(1,odd) 2,even 3,odd
lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,31)]
print(lst)

###
string='luminartechnolab'
#l====>n
#u====>y
#m====>n
vowels='aeiou'
lst=['y' if i in vowels else 'n' for i in string]
print(lst)