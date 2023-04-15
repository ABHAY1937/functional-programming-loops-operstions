#lower
#upper
#sum of even numbers

lower=int(input("enter lower limit"))
upper=int(input("enter uppper limit"))

sum=0
while(lower<=upper):
    if(lower%2==0):
       sum+=lower
    lower+=1
print(sum)



