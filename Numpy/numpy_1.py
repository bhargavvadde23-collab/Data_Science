#python lists are flexible but slow for large computational operations
#Numpy's can easily solve varieties of ,,
#Numpy performs these operations faster because data stored in contiguous memory
'''
1)Mathematical operations ex-- add,mul,sub,power,division, floor,etc...
2)Statistical functions ex--mean,median,std deviation, variance,mode...
3)Universal functions ex--sin,cos,log,sqrt,exp.....
4)Matrix operations like ex--1D,2D, and nD arrays with their operations
5)Random module ex-generate random values
6)Boolean indexing ex--


'''

#problem arises because we cannot assign values to the empty list , it throws an index out
#of range error
'''
a=[1,2,3,4]
b=[2,3,4,5]

c=[]

for i in range(len(a)):
    
    c[i]=a[i]+b[i]
    
    
print(c)
'''


#Best ways to fix this is ----append
'''
a=[1,2,3,4]
b=[2,3,4,5]

c=[]

for i in range(len(a)):
    
    c.append(a[i]+b[i])
    
print(c)
'''



#2) creating five zeroes in the c list
'''
a=[1,2,3,4]
b=[2,3,4,5]

c=[0] * len(a)

for i in range(len(a)):
    c[i]=a[i]+b[i]

print(c)
'''





#Using numpy
#1D-array
'''
import numpy as np

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a+b)
'''

#2D-array
'''
import numpy as np

a=np.array(
    [[1,2,3],
     [2,3,4]]
)

print(a)
print(a.shape)   # returns rows,cols
print(a.ndim)   # returns no.of dimensions
print(a.size)   # returns total no.of elements
print(a.dtype)  #returns datatype of the elements
print(a.itemsize) #returns memory occupied by one element
'''




