#biary_search

#1.lst=[6,1,10,15,25,9,5,22,19,35,21]

# 1. SORT THE GIVEN LIST[ascending order]

#lst=[1,5,6,9,10,15,19,21,22,25,35]
#     low                         upp
#2. low=0
#  upp=len(lst)-1             #upp=10

#3.caculate mid

#mid=(low+upp)//2  #

#mid=(0+10)//2=5

#check 3 conditions
    #A.searching_element>list[mid]  21>
        #low=mid+1
    #B. searching_element<lst[mid]
        #upp=mid-1
    #C. searching_element==lst[mid]
         #element_found
flag=0
element=int(input('enter a number'))
lst=[22,21,31,2,3,54,32,98,78,62,98,70,30,20]
lst.sort()
low=0
upp=len(lst)-1

for i in range(low,upp+1):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1

    elif(element<lst[mid]):
        upp=mid-1

    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
        print('element found')
else:
        print('not found')


