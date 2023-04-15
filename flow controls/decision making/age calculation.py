#current year
#current month
#current date
#birth year
#birth month20
#birth date

#console display ur ===age

# cyear=int(input("enter the current year"))
# month=int(input("enter this month"))
# date=int(input("enter today's date"))
# byear=int(input("enter your birth year"))
# bmonth=int(input("enter your birth month"))
# bdate=int(input("enter your birth date"))
# age=cyear-byear
# if(bmonth==2):
#     print(28-bdate,'pending days')
# elif(bmonth==1,3,5,7,8,9,10):
#     print(date-bdate,'balance month')
# elif(bmonth!=0):
#     print(12-bmonth,"balance month")
# elif(byear!=cyear):
#     print(cyear-byear,'balance yr')
# age=print()


cyear = int(input("Enter the current year: "))
cmonth = int(input("Enter the current month: "))
cdate = int(input("Enter the current date: "))
byear = int(input("Enter your birth year: "))
bmonth = int(input("Enter your birth month: "))
bdate = int(input("Enter your birth date: "))

age = cyear - byear
if bmonth > cmonth or (bmonth == cmonth & bdate > cdate):
    age -= 1

print(f"Your age is: {age}")
