#interchanging first and last elements in a list
'''
list=[12,24,35,67,80]

list[0],list[-1]=list[-1],list[0]

print(list)
'''


#using list sicing
'''
list=[12,24,35,67,80]
list=list[-1:]+list[1:4]+list[:1]

print(list)
'''



#reverse a list
'''
list=[12,24,35,67,80]

list.reverse()
print(list)
   '''
   

#without using a loop
'''   
list=[12,24,35,80]
i,j=0,len(list)-1

while i<j:
    list[i],list[j]=list[j],list[i]
    i+=1
    j-=1

print(list)
'''


#multiplying elements in a list
'''
import math

list=[1,2,3,4,5]
mul=math.prod(list)
print(mul)
'''



#maximum element in the list
'''
def max_list(list):
    max=list[0]
    
    for i in list:
        if i>max:
            max=i
    return max

list=[1,2,3,4,5]

print("max element in the list :",max_list(list))     # or a=max(list)
'''



#max and minimum of two lists
'''
a=[1,2,3,4,5]
b=[6,7,8,9,10]

c=max(max(a),max(b))
d=min(min(a),min(b))

print("max:",c,"min:",d)
'''



#finding second largest
'''
a=[2,34,12,56,23,90]

a.sort(reverse=True)

print(a[1])
'''


#append at the begining using deque
'''
from collections import deque

a=deque([2,34,12,56,23,90])

a.appendleft(6)
print(list(a))
'''



#using insert
'''
a=[2,34,12,56,23,90]
a.insert(0,6)
print(a)
'''


#list intersection
'''
a=[1,2,3,4,2,3,6,7]
b=[9,8,0,7,2,3,4,2]

res=list(set(a)&set(b))

print(res)
'''




#list comprehension

#basic syntax  [expression for item to iterable]

#with condition  [expression for item to iterable if condition]

#Nested loops    [expression for item1 to iterable for item2 to iterable]

#Ex-1
'''
squares=[i**2 for i in range(10)]
print(squares)

#Ex-2

even=[i for i in range(10) if i%2==0]
print(even)
'''

'''

list1=[1,2,3,4]
list2=['a','b','c','d']

pair=[[i,j] for i in list1 for j in list2]
print(pair)
'''




#MOve left by 1 pos

'''
l1=[1,2,3,4,5]

first=l1[0]

for i in range(len(l1)-1):
    l1[i]=l1[i+1]
    
l1[-1]=first

print(l1)
'''



#Small trick when you remove the first element the new list is created 2,3,4,5 with indexes
#0,1,2,3 loop goes to the next iteration
'''
num=[1,2,3,4,5]

for n in num:
    if n<3:
        num.remove(n)

print(num)
'''





#Moving all zeroes to the left in a list

#J is used to keep track of zeroes so in 6th iteration l[5],l[3]=l[3],l[5]

'''
l=[0,1,2,3,0,4]

j=0

for i in range(len(l)):
    if l[i]!=0:
        l[i],l[j]=l[j],l[i]
        j+=1
        
print(l)
'''
