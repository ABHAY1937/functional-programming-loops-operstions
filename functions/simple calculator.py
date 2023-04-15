#create a simple calculater using functions 3rd method is used here

#addition
#substration
#3.multiplication
#4.division

#enter your choice 1

#enter num1
#enter numb2
#addition result is

def add(num1,num2):
    sum=num1+num2
    return sum
def sub(num1,num2):
    substraction=num1-num2
    return substraction
def multi(num1,num2):
    multiply=num1*num2
    return multiply
def div(num1,num2):
    divis=num1/num2
    return divis


print("1.Addition\n","2.Substraction\n","3.Multiplication\n","4.Division")
choice=int(input('enter your choice'))
num1 = int(input("enter number1"))
num2 = int(input("enter number 2"))

if(choice==1):
    print(num1,"+",num2,'=',add(num1,num2))

elif(choice==2):
    print(num1, "-", num2, '=', sub(num1, num2))
elif(choice==3):
    print(num1, "*", num2, '=', multi(num1, num2))
elif(choice==4):
    print(num1, "/", num2, '=', div(num1, num2))
else:
    pass