#method 1 to declare array using Array Module 

from array import *
a1 = array('i',[1,2,3,45,6])

for i in range(len(a1)):
    print(a1[i],end = ' ')
    
    #method 2 to declare array using numpy library
from numpy import *

a2= array([1,2,3])
print('\n')
for i in range(len(a2)):
    print(a2[i],end=' ')

#methods Perormed on array
print("\n")

a1.append(1)

print("\n")    
print(a1.count(1))
print(a1.index(1))
a1.pop()
a1.reverse()
for i in range(len(a1)):
    print(a1[i],end=" ")
    






