#country count
f=open("C:/Users/Dell/Documents/.unknown",'r')
dic={}
for i in f:
  data=i.rstrip('\n').split(",")

  coun= data[-1]
  if coun not in dic:
    dic[coun]=1
  else:
    dic[coun]+=1
for k,v in dic.items():
    print(k,':',v)

