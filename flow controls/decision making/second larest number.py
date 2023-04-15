# find the second largest number from the following

num1=int(input("enter number 1"))#100
num2=int(input("enter number 2"))#80
num3=int(input("enter number 3"))#60
#nested if
if(num1>num2)&(num1>num3):#100>80 & 100>60
    if(num2>num3):
        print("number 2 is second largest",num2)
    else:
        print("num3 is second largest",num3)
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print("num1 is second largest",num1)
    else:
        print("number 3 is second largest",num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print("num1 is second largest",num1)
    else:
        print("num2 is second largest",num3)
else:
    print(" ")
