
#temperature
#kannur30
#palakad31
#district=data[0] #kannur
#tem=data[1]  30

#kannur30
#palakad31
# 2 tavana varumbo higher temp consider cheiyanm

f=open("C:/Users/Dell/Documents/temper.unknown",'r')
dic={}
for i in f:
    data=i.rstrip('\n').split(",")
    district=data[0]
    temperature=[1]

    if district not in dic:
       dic[district]=temperature
    else:
        old=dic[district]
        if(temperature>old):
           dic[district]=temperature
print(dic)