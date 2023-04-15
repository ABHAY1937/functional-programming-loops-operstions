#1.after 2000 released movie name year rating
f = open('C:/Users/Dell/Documents/movies.csv', 'r')
for i in f:
    data = i.rstrip('\n').split(',')
    if(data[-2]>'2000'):
        print(data)
