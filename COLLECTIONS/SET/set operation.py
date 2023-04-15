#set operation

#1.Union = all elements except dupicates

#2. Intersection === only duplicates elemnts are given

#3. Difference == (A-B) A_il element present arikum ennal B_il kanaruth
# (B-A)====> here elements present in set   B  are not present in set A

st1={1,2,3,4,5,6,7,8,9}
st2={5,6,4,7,8,91,2,3,5,5}

#union={12345678991}
st3=st1.union(st2)
print(st3)

#intersection
st3=st1.intersection(st2)
print(st3)

#difference
st3=st1.difference(st2)
print(st3)

st4=st2.difference(st1)
print(st4)