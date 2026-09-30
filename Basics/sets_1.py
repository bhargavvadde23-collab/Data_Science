#Sets in python means collection of unordered elements , they do not follow any speicic order.
#Also sets do not allow any duplicate elements
#sets are useful for Membership Tests and mathematical operations like intersection ,union , or, and etcc

my_set=set()
print(type(my_set))

#Basic set operations
'''
my_set=set([1,2,3,4,4,3,5,6])

print(my_set)

my_set.add(8)

print(my_set)


my_set.remove(3)
print(my_set)

my_set.discard(10)      #removes only if 10 present,otherwise it is a exception
print(my_set)

removed_element=my_set.pop()
print(removed_element)

my_set.clear()
print(my_set)
'''

#Membership operator
'''
s1={1,2,3,4,2,3,5}

print(1 in s1)
print(10 in s1)
print(2 in s1)
'''



#Mathematical operations
'''
s1={1,2,3,4,5,6}
s2={6,7,3,8,9,1}

set_union=s1.union(s2)
print(set_union)

intersection_set=s1.intersection(s2)
print(intersection_set)


s1.intersection_update(s2)      #set1 gets updated to intersection_set
print(s1)
'''



'''
s1={1,2,3,4,5,6}
s2={6,7,3,8,9,1}

print(s1.difference(s2))        #s1-s2

print(s2.difference(s1))        #s2-s1

print(s1.symmetric_difference(s2))      #common elements are removed


print(s1.issubset(s2))

print(s1.issuperset(s2))
'''

'''
text="rajiv gandhi university"
words=text.split()

unique_words=set(words)
print(unique_words)
print(len(unique_words))

'''





