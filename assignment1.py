# given an array with some integer type values. write a python script to sort array values?

from array import *
arr = array('i',[1,5,3,4,5,6])
a2=sorted(arr)
print(a2)

# given a list of hetrogeneous elements. write a python script to remove all the non int values from the list?
li=[1,2,'fenil','some',True,'no',1,2,3,42,'yes']
li2=[]
for i in li:
    if isinstance(i,int) and not isinstance(i,bool):
        li2.append(i)
print(li2)
        

# write a python script to calculate average of elements of list.
ele = [2,3,4,5,2,3,4,2,3]
average=int(sum(ele)/len(ele))
print("The average of the given number in this list is:",average)

# write a python script to create a list of first N fibonacci series

n= 10
fib=[0,1]
for i in range(n-2):
    fib.append(fib[-1]+fib[-2])
print(fib)

# write a python script to create a list of first N prime numbers.

n = int(input("Enter the number till which you want to get Prime numbers:"))
for i in range(1,n):
    if i >1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)

