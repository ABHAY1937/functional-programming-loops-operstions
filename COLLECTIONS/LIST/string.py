string='luminartechnolab is it finishing school'

#count number of consonants

vowels='aeiou'
lst=[]
for i in string:
    if( i not in vowels):
        lst.append(i)
print(lst)
print(len(lst))

