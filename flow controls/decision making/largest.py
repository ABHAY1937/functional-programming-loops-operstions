#read 3 numbers from consol
#num1
#num2
#num3


num1=int(input("enter  numbers1")) #100
num2=int(input("enter  numbers2"))  #80
num3=int(input("enter  numbers3")) #60
if(num1>num2)&(num1>num3): #80>60 & 80>100
    print("greatest number",num1)
elif(num2>num1)&(num2>num3): #60>80 & 60>100
    print("greatest number",num2)

else:
    print("number 3 is largest",num3)


