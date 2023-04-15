#each profession count
f=open("C:/Users/Dell/Documents/.unknown",'r')
dic={}

for i in f:
    data=i.rstrip('\n').split(' ')
    prof=data[-1]

    if(prof not in dic):
         dic[prof]=1
    else:
        dic[prof]+=1
for k,v in dic.items():
    print(k,':',v)



#each country



