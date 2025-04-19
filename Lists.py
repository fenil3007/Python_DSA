# list implementation in python
l1= [1,2,3,4,3,5]
# print(l1)
# print(type(l1))

l2=[1,3,4,6,7]
l1.extend(l2)
# print(l1)

l1.sort()
# print(l1)

l1.insert(1,3)
l1.remove(3)
l3=l1.copy()
print("The count of occurance of 3 is:",l1.count(3))
l1.reverse()
print(l1)
print(l3)