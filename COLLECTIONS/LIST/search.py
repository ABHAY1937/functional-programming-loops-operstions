lst=[14,13,465,65,75,87,99,33,11,32,68,97,99]

#read an element
flag=0
element=int(input("enter an element from the list"))
for i in lst:
    if(element==i):
        flag=1
        break
if(flag>0):

    print("element present")

else:
        print("not present")
# this search method is called 'linear search algorithm'
#draback===> its has high time complexity
#to overcome this we use 'binary search'