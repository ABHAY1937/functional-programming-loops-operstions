#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#If student is allowed to sit in exam or not.

total=int(input("total class held"))
attended=int(input("total class attended"))
percnt= (attended/total)*100

print("percentage of class attended",percnt)
if(percnt>=75):
    print('you can write the exam')
elif(percnt<75):
    print("better luck next time")
else:
    print(" ")
