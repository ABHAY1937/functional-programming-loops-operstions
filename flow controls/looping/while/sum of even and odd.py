#lower
#upper
#lower to upper even sum
#odd sum

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
even_sum=0
odd_sum=0
while(lower<=upper):#1<=5 2<=5 3<=5 4<=5
    if(lower%2==0):#1%2==0 2%2==0
       even_sum+=lower #0+2=2
    else:
        odd_sum+=lower
    lower+=1
print("evensum=",even_sum)
print("odd_sum",odd_sum)

