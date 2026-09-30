#Dictionaries in python are key-value pairs , unordered collection of elements , keys must be immutable



#Formatted String-it is a way of inserting the variables into the string,if different datatypes are present
'''
name="bhargav"
age=20

print(f"hi i am {name} and i am {age} years old")


name="bhargav"
print(f"{name:>10}")        #right aligns the text with 10 field width
'''


#creating an empty dictionary
'''
my_dict={}

my_dict2=dict()

print(my_dict)
print(my_dict2)
'''



'''

d1={
    "name":"bhargav",
    "age":22,
    "grade":'A',
    "roll_no":61
}

#Accesing elements

print(d1["name"])
print(d1["age"])

#using get()

print(d1.get("name"))
print(d1.get("roll_no"))
print(d1.get("last"))                   #returns none
print(d1.get("lst","not available"))    #returns not available
'''


#dictionary methods
'''
d1={
    "name":"bhargav",
    "age":22,
    "grade":'A',
    "roll_no":61
}

print(d1.keys())
print(d1.values())

print(d1.items())
d2=d1.copy()
print(d2)
'''

#Nested dictionaries
'''
d1={
    "stu1":{"name":"bhargav","age":22},
    "stu2":{"name":"peter","age":20}

}

print(d1["stu2"]["name"])


#iteration through nested dictionaries

for stu_id,stu_info in d1.items():
    print(f"{stu_id}:{stu_info}")
    for key,value in d1.items():
        print(f"{key}:{value}")
'''


#Dictionary comprehension
'''
squares={x:x**2 for x in range(10)}
print(squares)

evens={x:x**2 for x in range(10) if x%2==0}
print(evens)
'''




#frequency of numbers
'''
num=[1,2,2,3,3,3,4,4,4,4]
freq={}

for i in num:
    if i in freq:
        freq[i]+=1
        
    else:
        freq[i]=1
print(freq)

'''

#Merging two dictionaries
'''
d1={'a':1,'b':2}
d2={'b':3,'c':4}

merged={**d1,**d2}          #using unpacking method
print(merged)

d1.update(d2)
print(d1)
'''


