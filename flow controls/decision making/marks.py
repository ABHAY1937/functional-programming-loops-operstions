#4subjects
#sun1
#sub32
#sub3
#sub4

#total

#180+  ====>A+
#160-179   A
#140-159 B+
#120-139 B
#100-119 C+
#80-99 C
#BELOW 80 fail

sub1=int(input("enter mark of subject 1"))
sub2=int(input("enter mark of subject 2"))
sub3=int(input("enter mark of subject 3"))
sub4=int(input("enter mark of subject 4"))
total=sub1+sub2+sub3+sub4
if(total>180):
    print("A+")
elif(total>=160)&(total<=179):
    print("A")
elif(total>=140)&(total>=139):
    print("B+")
elif(total>=120)&(total>=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(total>=80)&(total<=99):
    print("C")
elif(total<80):
    print("FAIL")
else:
    print(" ")

