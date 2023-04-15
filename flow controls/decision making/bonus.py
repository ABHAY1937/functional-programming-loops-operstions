#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

salary=int(input("enter your salary"))
year=int(input("enter your service "))
bonus=(salary*5)/100



if(year>=5):
    print("you will get 5% as net bonus as",bonus)
elif(year<5):
    print("no bonus")
else:
    print( )