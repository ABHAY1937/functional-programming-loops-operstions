st={10,2,35,5,78,54,25,45}

#how to remove element

# remove function is used here
st.remove(5)
print(st)

#discard ===> it is used to delete an element
st.discard(10)
print(st)

#difference between remove and discard
#remove === retun type anu error mention cheyum
#but in discard no retrn type so no error has been shown
#eg
st.discard(100)
print(st)
st.remove(100)
print(st)