#word count

#rat,cat,bat,rat,cat,bat,bat,cat,rat,rat

#rat=4
#cat=3
#bat=3
#this kind of problem is word count

line='rat cat bat bat cat bat rat cat rat bat cat rat bat cat cat rat cat bat'
#dic={}
#key value
#cat
#rat
#bat
data=line.split(" ") #line by line data split cheith words akn split fn use cheyam
dic={}

for i in data:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)