f=open('a para','r')
dic={}

for i in f:
    data=i.rstrip('\n').split(' ')

    for j in data:
      if(j not in dic):
          dic[j]=1
      else:
          dic[j]+=1
for k,v in dic.items():
    print(k,':',v)


