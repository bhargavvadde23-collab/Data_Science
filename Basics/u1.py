'''
def area(radius):
    a=3.14*(radius**2)
    return a

print(area(5))
'''


'''
my_list=["happy",[1,2,3,4]]

print(my_list[0][2])
'''


'''

l=[5,1,2,6,10,11,23,44]

max=l[0]
min=l[0]

for i in l:
    if i > max:
        max=i
    if i < min:
        min=i
        
print("maximum element is :",max)
print("minimum element is :",min)

'''



#vowel count

'''
str="aeiou"

c=0

for i in str:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c+=1
        
print("vowels count is:",c)
'''



#sum of the digits

'''
a=4567

b=0
r=0

while a>0:
    r=a%10
    b+=r
    a=a//10
    
print(b)

'''




#to understand the innerloop

'''
l1=[]
l2=[]

for i in range(5,10):
    for j in range(i):
        l1.append(j)
    l2.append(i)
    
print(l1)
print(l2)
'''
    
    
        
        
        
#most frequent element
'''
def most_freq(lst):
    max_count=0
    element=0
    
    for i in lst:
        count=0
        for j in lst:
            if i==j:
                count+=1
        if count>max_count:
            max_count=count
            element=i
    return element

lst=[1,2,2,3,4,5,1,2,4,5]

print("the most repeated element is:",most_freq(lst))
'''



#frequency of each element
'''
def freq(str):
    d={}
    
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

str="banana"

print("frequency of the elements are:",freq(str))
'''

    
            
            
#reverse a string
'''
def rev(str):
    result=""
    
    for i in range(len(str)-1,-1,-1):
        result=result+str[i]
    return result                           #if we add return result==str we get palindrome

str="bhargav"

print("reversed string is: ",rev(str))
   '''
   
   
   
   
#factorial
'''
def fact(n):
    if n==0:
        return 1
    val=1
    
    for i in range(1,n+1):
        val*=i
    return val

print("factorial of the number:",fact(5))
'''




#fibonacci series 
'''
def fib(n):
    a,b=0,1
    
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        
fib(10) 
'''




#prime
'''
def prime(n):
    
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

print(prime(12))
'''



#Datetime module 
'''

from datetime import datetime,timedelta

now=datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday)
'''

import time

print(time.time())
time.sleep(2)
print(time.time())


