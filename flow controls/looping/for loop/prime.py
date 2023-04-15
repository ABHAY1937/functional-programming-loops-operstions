#check given number is prime or not
#prime number 2,3,5,7,9,11,13,17,19,23...

num=int(input("enter a number")) #9
flag=0
for i in range(2,num):
    if(num%i==0): #9%2==0
         flag=1
if(flag>0):
    print("not prime")
else:
    print("number is prime")