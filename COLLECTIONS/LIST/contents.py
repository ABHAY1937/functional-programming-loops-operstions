#empty list
lst=[]
print(lst)

#adding a new element we use: append
lst.append(10)  #append used here
lst.append(80)
lst.append(90)
lst.append("pashuu")
print(lst) # add ony single element at a time

#for adding multiple element in a list we use : extend

# diff betwn append and extend must be asked in some cases so look throughly

lst.extend([10,3,78,88])  #extend is used here
print(lst)

# we can add values in specific position by using : insert
lst.insert(0,80) # first postion , then value
lst.insert(4,99)
lst.insert(5,0)
print(lst)

