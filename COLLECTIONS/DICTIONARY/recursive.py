pattern='ABDFBCDFGHYTHJKLMNORP'

#First recursive charactor
#B

dic={}
for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print("first recursive charactor",i)
        break



