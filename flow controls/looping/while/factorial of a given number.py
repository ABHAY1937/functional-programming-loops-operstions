#factorial of a number
#num
#factorial 5!=1*2*3*4*5

num=int(input("enter a number"))
i=1
fact=1
while(i<=num):
     fact*=i
     i+=1
print(fact)
