# 0
# 0 2 4
# 0 3 6 9
# 0 4 8 12 16

for i in range(2,6):
    for j in range(0,(i-1)*2):
        print(j*i,end=" ")
    print()