
#1.after 2000 released movie name year rating
#2. 1975 and 2000 moves name year rating
#3. rating abopve 4 movies name year rating
#4. rating 3.5 and 4 movie name year rating
#5. each year release movie count

#Answer1.
f=open('C:/Users/Dell/Documents/movies.csv','r')
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[-3]
    if year >'2000':
        print(data[1:4])
#2
for i in f:
    data=i.rstrip('\n').split(',')
    year=data[-3]
for f in range(1975,2001):
        print(data[1::2])
#3.
for j in f:
    data=j.lstrip('\n').split(',')
    rate=data[-2]
    if rate>='4':
       print(data[1:])


