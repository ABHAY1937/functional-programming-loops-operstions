string="luminartechnolab"
vowels="aeiou"
lst=[]
for i in string:
    if(i in vowels):
        lst.append(i)
print(lst)
print(len(lst))