#lower
#upper
#sum of even numbers and odd numbers from lower to upper

lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
even_sum=0
odd_sum=0
for i in range(lower,upper+1):
    if(i%2==0):
        even_sum+=1
    else:
        odd_sum+=1

print("even_sum is",even_sum)
print("odd_sum is",odd_sum)

