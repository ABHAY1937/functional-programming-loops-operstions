#Assaignment
#string='practice problems to drill list comprehension in your head'

#1.create a list from 1 to 1000
#2. find all of the numbers from 1 to 1000 that are divisble by 8
#3. find all of the numbers from 1 to 1000 that have 6 in them
#4. count number of spaces in string
#5.count numbers of vowels
#6.remove all of the vowels in a string
#7 find all of the word in a sting that are less than 5 letters
#1
lst=[i for i in range(1,1001)]
print(lst)
#2
lst2=[i for i in lst if i%8==0]
print(lst2)
#3
lst=[i for i in lst if '6' in str(i) ]
print(lst)
#4
#[ i for in string if ==" "]
string='practice problems to drill list comprehension in your head'
count = len([i for i in lst for j in lst if i in 'aeiou'])
print(count)



#7
#
string='practice problems to drill list comprehension in your head'
words=string.split(" ")
print(words)
lst=[i for i in words if len(i)<5 ]
print(lst)