list=[1,2,3,4,5,8,8,7]
a=[1,2,3,4,5,8,7,7,7]
print(list.count(8))
print(list)
#to add samething in list
list.append(6)
print(list)
#to short list in ascending or descending order
list.sort()#for ascending
print(list)
a.sort(reverse=True)#for descending or
print(a)
a.reverse()#for descending
print(a)
#to find  index of a elements in list 
print(a.index(7))
#to count the occurence of the element
print(a.count(7))
#to copy a list in 
b=a.copy()
#how to copy the list
b.insert(1,555)
print(b)
#how to merge two  lists 
a.extend(b)
print(a)


