f = open('C:/Users/Dell/Documents/movies.csv', 'r')

for i in f:
    data = i.rstrip('\n').split(',')
    year = data[-3]
    rating=data[-1]
    if year == '2008' and data[-1]>'3':
        print(data[1:4])
#1.append cheithitu len cheitha row count kitum

    count = 0
    for line in f:
        count += 1

print("Number of rows:", count)

#2 removing duplicate elements and row count
with open('C:/Users/Dell/Documents/movies.csv', 'r') as f:
    lines = set()
    for line in f:
        lines.add(line)

count = len(lines)
print("Number of unique lines:", count)

with open('C:/Users/Dell/Documents/movies.csv', 'w') as f:
    for line in lines:
        f.write(line)

