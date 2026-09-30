#Creating arrays

'''
import numpy as np

a=np.zeros((2,3))   #prints matrix of zeros

print(a)

b=np.ones((2,2))

print(b)            #prints matrix of ones

c=np.full((2,3),7)

print(c)            #prints matrix of desired values

d=np.eye(4)

print(d)               #prints identity matrix
'''


'''
import numpy as np

a=np.arange(1,15,3)

print(a)

b=np.array([1,2,3,4],dtype=float)

print(a)
'''



#Slicing a n-dimensional array
'''
import numpy as np

# Create a 4x4 array with numbers 10 through 25
arr = np.array([
    [10, 11, 12, 13],
    [14, 15, 16, 17],
    [18, 19, 20, 21],
    [22, 23, 24, 25]
])

print(arr[:2 , :2])
print(arr[2: , 2:])

print(arr[1:3 , 1:3])

print(arr[:2 , 2:])

#to print individual numbers we use [0,3] selecting particular columns

print(arr[1:3 , [0,3]])

print(arr[2:4 , [1,3]])  # or arr[2:4 , 1::2] it is a step function

print(arr[1:2 , :1])    #14

print(arr[2:3 , 3:])   #21
'''




#Universal functions
'''
import numpy as np

a=np.sqrt([4,5,6,7])
print(a)

b=np.sin(a)
print(b)

c=np.cos(a)
print(c)

d=np.log(a)
print(d)

e=np.exp(a)
print(e)
'''



#Statistical functions

import numpy as np

a=np.array([10,20,30,40])

c=np.mean(a)
print(c)


d=np.median(a)
print(d)

e=np.mode(a)
print(e)
