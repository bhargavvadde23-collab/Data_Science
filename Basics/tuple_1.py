#tuple is a immutable ordered collection of elements , once it is written they cannot be changed

'''
t1=(1,2,3,"apple",True)

print(t1)
print(type(t1))
'''


'''
t1=(1,2,3,"apple",True)
print(t1[0])
print(t1[2])
print(t1[-1])


print(t1[:4])

print(t1[::2])

print(t1[::-1])

'''

'''
t1=(1,2,3,"apple",True)
t2=(1,2,3,4,5)

print(t1+t2)
print(t1*3)
'''


#Tuple methods
'''
t1=(1,2,3,"apple",True)
t2=(1,2,3,4,5)

print(t1.count(1))
print(t2.index(4))
'''

#packing the tuple

pack=1,2,"hello",3.14
print(pack)

#unpacking the tuple
#Ex-1
a,b,c,d=pack

print(a)
print(b)
print(c)
print(d)

#Ex-2
first,*middle,last=pack
print(first)
print(middle)
print(last)






