#lower
#upper

#even numbers

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))

i=1
while(lower<=upper):
    if(lower%2==0):
        print(lower)
    lower+=1