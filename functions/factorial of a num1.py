#find factorial of a number

#method1

def fact():
    num = int(input("enter a number"))
    i = 1
    facto = 1
    while (i <= num):
        facto *= i
        i += 1
    print(facto)
fact()
fact()

